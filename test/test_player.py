import unittest
from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("TestPlayer")

    def test_init(self):
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(self.player.score, 0)

    def test_add_to_score(self):
        self.player.add_to_score(10)
        self.assertEqual(self.player.score, 10)

    def test_reset_score(self):
        self.player.add_to_score(10)
        self.player.reset_score()
        self.assertEqual(self.player.score, 0)

if __name__ == '__main__':
    unittest.main()
