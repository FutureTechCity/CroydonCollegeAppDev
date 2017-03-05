
import unittest

from rock_paper_scissors.main import RPS, Outcome, Rules, Game


class GameTests(unittest.TestCase):
    def setUp(self):
        rules = Rules()
        self._game = Game(rules)

    def test_game(self):
        expected = list(Outcome.__members__.values())

        result = self._game.play(RPS.rock)
        assert result in expected

        result2 = self._game.play(RPS.paper)
        assert result2 in expected

        result3 = self._game.play(RPS.scissors)
        assert result3 in expected


if __name__ == '__main__':
    unittest.main()