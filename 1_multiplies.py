"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import unittest
from functools import reduce


def first_task(num: int):
    return reduce(
        lambda x, y: x + y,  # failed if num is 0
        # filter(lambda x: x % 3 == 0 or x % 5 == 0, list(range(num)))
    )


def first_task_second(num: int):
    return sum(i for i in range(num) if i % 3 == 0 or i % 5 == 0)


class TestFirstTask(unittest.TestCase):
    def test_first_task(self):
        data = [
            (10, 23),  # (num, sum of all natural numbers below 'num')
            (1000, 233168)
        ]
        for num, result in data:
            self.assertEqual(first_task(num), result)
            self.assertEqual(first_task_second(num), result)


if __name__ == '__main__':
    unittest.main()
