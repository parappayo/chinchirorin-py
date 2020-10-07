
import sys, random


def roll_generator(die_sides):
    while True:
        yield random.randint(1, die_sides)


def roll(num_dice, die_sides):
    rolls = roll_generator(die_sides)
    return [next(rolls) for i in range(num_dice)]


if __name__ == "__main__":
    num_dice, die_sides = 1, 6

    if len(sys.argv) > 1: num_dice = int(sys.argv[1])
    if len(sys.argv) > 2: die_sides = int(sys.argv[2])

    print(f"{num_dice}d{die_sides}={roll(num_dice, die_sides)}")
