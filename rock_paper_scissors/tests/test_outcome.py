
import unittest

from rock_paper_scissors.main import RPS, Outcome


class OutcomeTests(unittest.TestCase):
    def test_rock(self):
        result = Outcome.calculate(RPS.rock, RPS.paper)
        assert result == Outcome.right_hand_wins

        result2 = Outcome.calculate(RPS.paper, RPS.rock)
        assert result2 == Outcome.left_hand_wins

        result3 = Outcome.calculate(RPS.scissors, RPS.rock)
        assert result3 == Outcome.right_hand_wins

        result4 = Outcome.calculate(RPS.rock, RPS.scissors)
        assert result4 == Outcome.left_hand_wins

        result5 = Outcome.calculate(RPS.rock, RPS.rock)
        assert result5 == Outcome.draw


if __name__ == '__main__':
    unittest.main()