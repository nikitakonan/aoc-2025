import unittest
from .task_2 import find_max_joltage

test_cases = [
  ("987654321111111", 987654321111),
  ("811111111111119", 811111111119),
  ("234234234234278", 434234234278),
  ("818181911112111", 888911112111),
]

class TestFindMaxJoltage(unittest.TestCase):
    def test_cases_from_list(self):
        for input_str, expected in test_cases:
            with self.subTest(input_str):
                actual = find_max_joltage(input_str)
                self.assertEqual(actual, expected)


