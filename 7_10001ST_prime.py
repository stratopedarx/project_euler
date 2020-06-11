"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from itertools import count

from tasks.utils import count_time


NUMBER = 10001


def is_prime(n):
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


@count_time
def get_prime_number_by(num: int) -> int:
    k = 0
    for c in count(1, step=2):  # we won`t check even numbers
        if is_prime(c):
            k += 1

            if k == num:
                return c


print(get_prime_number_by(NUMBER))
