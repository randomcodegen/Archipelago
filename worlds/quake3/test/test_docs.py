from pathlib import Path
import unittest

from .. import Quake3World


class TestDocumentation(unittest.TestCase):
    def test_registered_tutorial_and_game_info_exist(self):
        docs = Path(__file__).resolve().parents[1] / "docs"
        self.assertTrue((docs / f"en_{Quake3World.game}.md").is_file())
        self.assertEqual(len(Quake3World.web.tutorials), 1)
        tutorial = Quake3World.web.tutorials[0]
        self.assertEqual(tutorial.file_name, "setup_en.md")
        self.assertIn("**Singleplayer**", (docs / tutorial.file_name).read_text(encoding="utf-8"))
