from tasks.utils import count_time


@count_time
def sum_square_difference(num: int) -> int:
    lst = list(range(1, num + 1))
    sum_of_squares = sum(i ** 2 for i in lst)
    square_of_sum = sum(i for i in lst) ** 2

    return square_of_sum - sum_of_squares


print(sum_square_difference(100))
