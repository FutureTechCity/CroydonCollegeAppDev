"""
An implementation of Rock-Paper-Scissors in python, for teaching purposes.

Note that there are no string comparisons or if:else statements in this code.
"""


from enum import Enum
import random


class Hand:
    def __init__(self):
        self._better_than = None
        self._worse_than = None

    def __eq__(self, other):
        return other.__class__ == self.__class__

    def __lt__(self, other):
        return other == self._worse_than

    def __gt__(self, other):
        return other == self._better_than

    def beats(self, item):
        self._better_than = item.hand
        item.hand.beaten_by(self)

    def beaten_by(self, item):
        self._worse_than = item


class Rock(Hand):
    pass


class Paper(Hand):
    pass


class Scissors(Hand):
    pass


class RPS(Enum):
    rock = Rock()
    paper = Paper()
    scissors = Scissors()

    def __init__(self, item):
        self._hand = item

    @property
    def hand(self):
        return self._hand


class Outcome(Enum):
    draw = (lambda x, y: x.hand == y.hand, 'Draw', 0)
    left_hand_wins = (lambda x, y: x.hand > y.hand, 'You win', 1)
    right_hand_wins = (lambda x, y: x.hand < y.hand, 'You lose', -1)

    def __init__(self, *items):
        self._predicate = items[0]
        self._text = items[1]
        self._score = items[2]

    @property
    def predicate(self):
        return self._predicate

    @property
    def text(self):
        return self._text

    @property
    def score(self):
        return self._score

    @classmethod
    def calculate(cls, left, right):
        values = cls.__members__.values()
        items = filter(lambda x: x.predicate(left, right), values)
        return next(items)


class Rules:
    def __init__(self):
        RPS.rock.hand.beats(RPS.scissors)
        RPS.scissors.hand.beats(RPS.paper)
        RPS.paper.hand.beats(RPS.rock)

    def decide_winner(self, left: RPS, right: RPS):
        return Outcome.calculate(left, right)


class Game:
    """
    Randomly chooses a `right hand` to oppose the user-defined
    `left-hand`
    """
    def __init__(self, rules: Rules):
        self._rules = rules

    def play(self, mine: RPS):
        computer = self._computer_hand()
        return self._rules.decide_winner(mine, computer)

    def _computer_hand(self):
        """ Modify this logic to have different
            computer behaviours. """
        return random.choice(list(RPS.__members__.values()))
