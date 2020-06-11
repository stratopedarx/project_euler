"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
https://foxford.ru/wiki/informatika/proverka-chisla-na-prostotu-v-python
"""
import unittest
from typing import List


def is_prime(num: int) -> bool:
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


def get_prime_numbers(num: int) -> List[int]:
    # https: // habr.com / ru / post / 122538 /
    lst = [2]
    for i in range(3, num + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


def calculate_largest_prime(num: int) -> int:
    res = get_prime_numbers(num)
    if res:
        return res[-1]
    return 0


def one():
    res = []
    x = 600851475143
    z = 2
    while z*z <= x:
        if x%z == 0:
            res.append(z)
            z +=1
        else:
            z+=1
    return res


res = []
for i in one():
    if is_prime(i):
        res.append(i)

print(res[-1])
