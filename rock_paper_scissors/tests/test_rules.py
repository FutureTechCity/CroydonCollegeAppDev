
import unittest

from rock_paper_scissors.main import RPS, Outcome, Rules


class RulesTests(unittest.TestCase):
    def setUp(self):
        self._rules = Rules()

    def test_rock(self):
        result = self._rules.decide_winner(RPS.rock, RPS.paper)
        assert result == Outcome.right_hand_wins

        result2 = self._rules.decide_winner(RPS.paper, RPS.rock)
        assert result2 == Outcome.left_hand_wins

        result3 = self._rules.decide_winner(RPS.rock, RPS.rock)
        assert result3 == Outcome.draw


if __name__ == '__main__':
    unittest.main()