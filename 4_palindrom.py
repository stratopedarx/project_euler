from itertools import product


def is_palindrom(num: int) -> bool:
    # num_str = str(num)
    # if len(num_str) % 2 != 0:
    #     return False
    # for i in range(len(num_str)):
    #     if num_str[i] != num_str[-1 - i]:
    #         return False
    # return True

    num_str = str(num)
    return num_str == num_str[::-1]


def make_3_digit_num():
    return list(range(999, 800, -1))


def get_max_3_digit_palindrom():
    list1 = make_3_digit_num()
    list2 = make_3_digit_num()

    for n1, n2 in  product(list1, list2):
        res = n1*n2
        if is_palindrom(res):
            return res

    return -1


# assert is_palindrom(99) is True
# assert is_palindrom(909) is False
# assert is_palindrom(9009) is True

print(get_max_3_digit_palindrom(), 'palindrom')

# done