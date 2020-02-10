ALL_PINS = 10
TOTAL_FRAMES = 10


class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total_score = 0
        roll_index = 0

        for frame in range(TOTAL_FRAMES):
            if self._is_strike(roll_index):
                total_score += ALL_PINS + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                total_score += ALL_PINS + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                total_score += self._frame_score(roll_index)
                roll_index += 2

        return total_score

    def _is_strike(self, roll_index):
        return self.rolls[roll_index] == ALL_PINS

    def _strike_bonus(self, roll_index):
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def _is_spare(self, roll_index):
        return self._frame_score(roll_index) == ALL_PINS

    def _spare_bonus(self, roll_index):
        return self.rolls[roll_index + 2]

    def _frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
