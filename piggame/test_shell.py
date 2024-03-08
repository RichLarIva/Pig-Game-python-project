import unittest
from unittest.mock import patch
from io import StringIO
from game import Game
from dice import Dice
from histogram import Histogram
from player import Player
from intelligence import Intelligence
from shell import Shell

class TestShell(unittest.TestCase):

    shell = Shell()
    shell.game = Game()
    shell.dice = Dice()
    shell.histgram = Histogram()
    shell.player_data = Player("TestPlayer")
    shell.ai = Intelligence()

    @patch('builtins.input', return_value="TestPlayer")
    def test_start(self, mocked_input):
        out = StringIO()
        with patch('sys.stdout', new=out):
            self.shell.do_start(None)
        output = out.getvalue().strip()
        self.assertIn("You will start throwing the dice.", output)

    def test_throw(self):
        out = StringIO()
        with patch('sys.stdout', new=out):
            self.shell.has_started = True
            self.shell.do_throw(None)
        output = out.getvalue().strip()
        self.assertIn("You rolled:", output)

    def test_switch_turn(self):
        out = StringIO()
        with patch('sys.stdout', new=out):
            self.shell.has_started = True
            self.shell.do_switch_turn(None)
        output = out.getvalue().strip()
        self.assertIn("The AI won", output)

    def test_show_histogram(self):
        out = StringIO()
        with patch('sys.stdout', new=out):
            self.shell.do_show_histogram(None)
        output = out.getvalue().strip()
        self.assertIn("Histogram", output)

    def test_score(self):
        out = StringIO()
        with patch('sys.stdout', new=out):
            self.shell.do_score(None)
        output = out.getvalue().strip()
        self.assertIn("Current scores", output)

    def test_cheat(self):
        out = StringIO()
        with patch('sys.stdout', new=out):
            self.shell.do_cheat(None)
        output = out.getvalue().strip()
        self.assertIn("So you want to cheat?", output)

    def test_exit(self):
        out = StringIO()
        with patch('sys.stdout', new=out):
            result = self.shell.do_exit(None)
        self.assertTrue(result)

    def test_rules(self):
        out = StringIO()
        with patch('sys.stdout', new=out):
            self.shell.do_rules(None)
        output = out.getvalue().strip()
        self.assertIn("The rules for this game are simple", output)

if __name__ == '__main__':
    unittest.main()
