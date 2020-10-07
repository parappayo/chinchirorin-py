import dice


def roll_3d6():
	"""Returns a random roll as if made by a player."""
	return dice.roll(3, 6)


def score_roll(roll):
	"""Determines the numerical score for the given roll."""
	return 0


def compare_rolls(roll1, roll2):
	"""Returns -1 if roll1 is larger, 1 if roll 2 is larger, 0 otherwise."""
	return 0


if __name__ == "__main__":
	print(roll_3d6())
