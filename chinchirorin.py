import dice


def roll_3d6():
    """Returns a random roll as if made by a player."""
    return dice.roll(3, 6)


def is_triple(roll):
    return roll[0] == roll[1] and roll[1] == roll[2]


def score_roll(roll):
    """Determines the numerical score for the given roll."""
    if is_triple(roll):
        return roll[0] + 10

    sorted_roll = sorted(roll)

    if sorted_roll[0] == sorted_roll[1]:
        return sorted_roll[2]

    if sorted_roll[1] == sorted_roll[2]:
        return sorted_roll[0]

    if sorted_roll == [1, 2, 3]:
        return -1

    if sorted_roll == [4, 5, 6]:
        return 20

    return 0


def compare_rolls(roll1, roll2):
    """Returns -1 if roll1 is larger, 1 if roll 2 is larger, 0 otherwise."""
    score1 = score_roll(roll1)
    score2 = score_roll(roll2)
    if score1 == score2:
        return 0
    elif score1 < score2:
        return 1
    return -1


class Roll():
    def __init__(self):
        self.roll = roll_3d6()

    def score(self):
        return score_roll(self.roll)

    def __sub__(self, other):
        if isinstance(other, Roll):
            return compare_rolls(self.roll, other.roll)
        return NotImplemented

    def __str__(self):
        die_chars = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
        roll_chars = list(map(lambda x: die_chars[x-1], self.roll))
        return ' '.join(roll_chars)


if __name__ == "__main__":
    player1_roll = Roll()
    player2_roll = Roll()
    result = player2_roll - player1_roll

    print(f"player 1 rolls {player1_roll}")
    print(f"player 2 rolls {player2_roll}")
    if result == 0:
        print("tie")
    elif result < 0:
        print("player 1 wins")
    else:
        print("player 2 wins")
