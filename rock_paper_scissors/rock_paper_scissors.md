# Rock-Paper-Scissors

This is an implementation of the simple rock-paper-scissors game in python,
designed purely for teaching purposes.

There are no strings, and no if:else: statements in the code, instead using a cyclic rock -> paper -> scissors -> rock object model to define relationships and relative behaviours.

# Running unit-tests

From the top-level of the repo, run

```python
python -m unittest discover
```

# Playing a game

The game logic is coded up in the `Rules` class. Pass this into the `Game` object, and call `play` with your selection:

```python
from rock_paper_scissors.main import Rules, Game, RPS

rules = Rules()
game = Game(rules)
game.play(RPS.rock)
```