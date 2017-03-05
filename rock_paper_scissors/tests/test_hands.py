
import unittest

from rock_paper_scissors.main import RPS, Rules


class HandsTests(unittest.TestCase):
    def setUp(self):
        self._rules = Rules()

    def test_rock(self):
        assert RPS.rock.hand > RPS.scissors.hand
        assert RPS.rock.hand < RPS.paper.hand
        assert RPS.rock.hand == RPS.rock.hand

    def test_paper(self):
        assert RPS.paper.hand > RPS.rock.hand
        assert RPS.paper.hand < RPS.scissors.hand
        assert RPS.paper.hand == RPS.paper.hand

    def test_scissors(self):
        assert RPS.scissors.hand > RPS.paper.hand
        assert RPS.scissors.hand < RPS.rock.hand
        assert RPS.scissors.hand == RPS.scissors.hand


if __name__ == '__main__':
    unittest.main()