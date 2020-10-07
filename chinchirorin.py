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
    #sorted_roll = sorted(roll)

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


if __name__ == "__main__":
    player1_roll = roll_3d6()
    player2_roll = roll_3d6()
    result = compare_rolls(player1_roll, player2_roll)

    print(f"player 1 rolls {player1_roll}")
    print(f"player 2 rolls {player2_roll}")
    if result == 0:
        print("tie")
    elif result < 0:
        print("player 1 wins")
    else:
        print("player 2 wins")
