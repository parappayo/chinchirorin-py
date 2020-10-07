import unittest, chinchirorin


score_roll_test_cases = [
    # { "roll": [1, 1, 2], "expected": 2 },
    # { "roll": [1, 3, 1], "expected": 3 },
    # { "roll": [4, 5, 5], "expected": 4 },
    # { "roll": [6, 6, 3], "expected": 3 },
    { "roll": [1, 1, 1], "expected": 11 },
    { "roll": [2, 2, 2], "expected": 12 },
    { "roll": [5, 5, 5], "expected": 15 },
    # { "roll": [1, 3, 5], "expected": 0 },
    # { "roll": [1, 2, 3], "expected": -1 },
    # { "roll": [4, 5, 6], "expected": 20 },
]


compare_rolls_test_cases = [
    # { "roll1": [1, 1, 2], "roll2": [1, 1, 3], "expected": 1 },
    # { "roll1": [1, 1, 3], "roll2": [1, 1, 2], "expected": -1 },
    # { "roll1": [3, 5, 6], "roll2": [2, 4, 5], "expected": 0 },
    # { "roll1": [3, 5, 6], "roll2": [3, 3, 5], "expected": 1 },
    # { "roll1": [5, 5, 6], "roll2": [3, 4, 5], "expected": -1 },
    # { "roll1": [5, 5, 6], "roll2": [1, 1, 1], "expected": 1 },
    { "roll1": [1, 1, 1], "roll2": [2, 2, 2], "expected": 1 },
    { "roll1": [3, 3, 3], "roll2": [3, 3, 3], "expected": 0 },
    { "roll1": [6, 6, 6], "roll2": [5, 5, 5], "expected": -1 },
    # { "roll1": [1, 2, 3], "roll2": [1, 2, 3], "expected": 0 },
    # { "roll1": [2, 3, 1], "roll2": [3, 2, 1], "expected": 0 },
    # { "roll1": [4, 5, 6], "roll2": [4, 5, 6], "expected": 0 },
    # { "roll1": [1, 2, 3], "roll2": [4, 5, 6], "expected": 1 },
    # { "roll1": [4, 5, 6], "roll2": [1, 2, 3], "expected": -1 },
    # { "roll1": [1, 1, 6], "roll2": [4, 5, 6], "expected": 1 },
]


class TestFunctions(unittest.TestCase):

    def test_roll3d6(self):
        roll = chinchirorin.roll_3d6()
        self.assertEqual(len(roll), 3)

    def test_score_roll(self):
        for test_case in score_roll_test_cases:
            self.assertEqual(
                chinchirorin.score_roll(test_case["roll"]),
                test_case["expected"])

    def test_compare_rolls(self):
        for test_case in compare_rolls_test_cases:
            self.assertEqual(
                chinchirorin.compare_rolls(test_case["roll1"], test_case["roll2"]),
                test_case["expected"])


if __name__ == "__main__":
    unittest.main()
