import unittest
from unittest.mock import patch
from io import StringIO
from intelligence import Intelligence

class TestIntelligence(unittest.TestCase):

    def setUp(self):
        self.ai = Intelligence()

    @patch('random.randint', side_effect=[1, 2])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_turn_switch_turn(self, mocked_stdout, _):
        rolls = self.ai.play_turn(True)
        output = mocked_stdout.getvalue().strip()
        self.assertNotIn("AI scored", output)
        self.assertIn("AI rolled", output)
        self.assertEqual(sum(rolls), self.ai.score)

    @patch('random.randint', side_effect=[2, 2, 1])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_turn_continue_throw(self, mocked_stdout, _):
        rolls = self.ai.play_turn(True)
        output = mocked_stdout.getvalue().strip()
        self.assertIn("AI rolled", output)
        self.assertIn("AI scored", output)
        self.assertEqual(sum(rolls), self.ai.score)

if __name__ == '__main__':
    unittest.main()
