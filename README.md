# TDD Demo - Bowling Game Kata

This repository forms part Software Development Practices
engineering training sessions. It contains a base project to run the bowling
game kata from.

## Branches

- `master` an empty project which can be used to practice/demonstrate the kata
- `completed` a branch with the completed code and a commit history detailing
  each step.
  
## Bowling Game Kata

The bowling game kata is a well known code kata. The aim is to use TDD to
implement a class which calculates the score of a 10 pin bowling game. The class
should have the following interface:

```python
class BowlingGame:
    def roll(self, pins):
        """
        Call this each time a ball is rolled passing in the number of pins that
        were knocked down.
        """

    def score(self):
        """
        Call this at the end of the game to get the final score.
        """
```

### Rules of 10 Pin Bowling

- A game has `10` frames
- A player has `2` rolls per frame to try and knock down all `10` pins
- If a player knocks down all `10` pins in a frame then they score a `spare`:
  - The score for a `spare` is the `10` pins plus the next roll as a bonus
- If a player knocks down all `10` pins in the first roll of a frame then they
  score a `strike`:
  - If a `strike` is scored then there is no second roll in the frame
  - The score for a `strike` is the `10` pins plus the next `2` rolls as a bonus
  - If a `strike` is scored in the last frame then `2` bonus rolls are added to
    the frame
- A perfect game is `12` successive `strikes` and scores `300` points

### Exceptions & Edge Cases

For a real implementation of this you would want to check for errors, including
the following:

- Negative number of pins passed to `roll`
- More than `10` pins passed to `roll`
- Score called before the game is completed
- Roll called too many times

However, for this demonstration we are only focussing on the happy path.

### Execution

We are using **pytest** lib for writing and running our Unit Tests.

Execute below command to run tests:
```ssh
make test
```
