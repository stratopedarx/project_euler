"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from tasks.utils import count_time


@count_time
def get_the_smallest_num(nums: tuple):
    start = 380  # 20 * 19 = 380. It is the biggest possible step
    while start:
        for i in nums:
            if start % i == 0:
                pass
            else:
                break
        else:
            print(f'We have found the smallest number: {start}')
            return start
        start += 380


get_the_smallest_num(tuple(range(20, 1, -1)))
