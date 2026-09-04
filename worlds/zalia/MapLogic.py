"""Export the installed AP rules as a small expression graph for the map HUD.

Only trusted Python rule code is compiled here, at generation time. The game
receives data (item counts, region references and arithmetic), never code.
"""
import ast
import copy
import inspect
from functools import reduce
from types import FunctionType, SimpleNamespace


class Expression:
    def __init__(self, op, *args):
        self.op, self.args = op, args

    def __bool__(self):
        raise TypeError("Map logic contains unsupported Python control flow")

    def __add__(self, other):
        return Expression("+", self, other)

    __radd__ = __add__

    def __ge__(self, other):
        return Expression(">=", self, other)


def _all(values):
    return reduce(lambda a, b: Expression("&", a, b), values, True)


def _any(values):
    return reduce(lambda a, b: Expression("|", a, b), values, False)


class _RuleSyntax(ast.NodeTransformer):
    def visit_BoolOp(self, node):
        return ast.copy_location(ast.Call(
            ast.Name("_map_all" if isinstance(node.op, ast.And) else "_map_any", ast.Load()),
            [ast.List([self.visit(v) for v in node.values], ast.Load())], []), node)

    def visit_UnaryOp(self, node):
        if isinstance(node.op, ast.Not):
            return ast.copy_location(ast.Call(ast.Name("_map_not", ast.Load()),
                                             [self.visit(node.operand)], []), node)
        return self.generic_visit(node)

    def visit_FunctionDef(self, node):
        # Normalize an early-return guard, as used by the boulder-circle rule.
        if (len(node.body) == 2 and isinstance(node.body[0], ast.If)
                and not node.body[0].orelse and len(node.body[0].body) == 1
                and isinstance(node.body[0].body[0], ast.Return)
                and isinstance(node.body[1], ast.Return)):
            guard = node.body[0]
            node.body = [ast.Return(ast.Call(ast.Name("_map_choose", ast.Load()),
                [guard.test, guard.body[0].value, node.body[1].value], []))]
        return self.generic_visit(node)

    def visit_GeneratorExp(self, node):
        # Count satisfied predicates without coercing symbolic values to bool.
        if (isinstance(node.elt, ast.Constant) and node.elt.value == 1
                and len(node.generators) == 1 and node.generators[0].ifs):
            node.elt = ast.Call(ast.Name("_map_all", ast.Load()),
                               [ast.List(node.generators[0].ifs, ast.Load())], [])
            node.generators[0].ifs = []
        return self.generic_visit(node)


def export_map_logic(world):
    regions = list(world.multiworld.get_regions(world.player))
    region_ids = {region.name: i for i, region in enumerate(regions)}
    compiled = {}
    sources = {}

    def convert(value):
        if isinstance(value, FunctionType):
            return compile_rule(value)
        if isinstance(value, tuple):
            return tuple(convert(v) for v in value)
        if value is world.multiworld:
            def get_location(name, player):
                location = value.get_location(name, player)
                return SimpleNamespace(can_reach=lambda state: _all((
                    state.can_reach_region(location.parent_region.name, player),
                    compile_rule(location.access_rule)(state))))
            return SimpleNamespace(get_location=get_location)
        return value

    def compile_rule(rule):
        if rule in compiled:
            return compiled[rule]
        module = inspect.getmodule(rule)
        if module not in sources:
            sources[module] = ast.parse(inspect.getsource(module))
        tree = sources[module]
        candidates = [n for n in ast.walk(tree)
                      if isinstance(n, (ast.FunctionDef, ast.Lambda))
                      and n.lineno == rule.__code__.co_firstlineno]
        if len(candidates) != 1:
            raise ValueError(f"Cannot export map rule {rule}: ambiguous source")
        node = copy.deepcopy(candidates[0])
        node.args.defaults = []
        node.args.kw_defaults = [None] * len(node.args.kwonlyargs)
        if isinstance(node, ast.Lambda):
            node = ast.FunctionDef("_rule", node.args, [ast.Return(node.body)], [], None)
        node.name = "_rule"
        node.decorator_list = []
        node.returns = None
        for arg in (*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs):
            arg.annotation = None
        closure = inspect.getclosurevars(rule)
        namespace = {**rule.__globals__, **{k: convert(v) for k, v in closure.nonlocals.items()}}
        namespace.update(all=_all, any=_any, _map_all=_all, _map_any=_any,
                         _map_not=lambda a: Expression("!", a) if isinstance(a, Expression) else not a,
                         _map_choose=lambda c, a, b: Expression("?", c, a, b))
        module = ast.fix_missing_locations(ast.Module([_RuleSyntax().visit(node)], []))
        exec(compile(module, "<map logic>", "exec"), namespace)
        result = namespace["_rule"]
        result.__defaults__ = convert(rule.__defaults__)
        compiled[rule] = result
        return result

    class State:
        def count(self, name, player):
            assert player == world.player
            return Expression("item", name)

        def has(self, name, player, count=1):
            return self.count(name, player) >= count

        def can_reach_region(self, name, player):
            assert player == world.player
            return Expression("region", region_ids[name])

    nodes, indices = [], {}

    def encode(value):
        if not isinstance(value, Expression):
            value = Expression("const", int(value))
        if value.op in ("const", "item", "region"):
            row = (value.op, *value.args)
        else:
            row = (value.op, *(encode(v) for v in value.args))
        if row not in indices:
            indices[row] = len(nodes)
            nodes.append(row)
        return indices[row]

    state = State()
    entrances = [(i, region_ids[edge.connected_region.name],
                  encode(compile_rule(edge.access_rule)(state)))
                 for i, region in enumerate(regions) for edge in region.exits
                 if edge.connected_region is not None]
    locations = [(loc.address, i, encode(compile_rule(loc.access_rule)(state)))
                 for i, region in enumerate(regions) for loc in region.locations
                 if loc.address is not None]
    return {"version": 1, "start": region_ids[world.origin_region_name],
            "region_count": len(regions), "nodes": nodes,
            "entrances": entrances, "locations": locations}
