"""
lucky numbers
"""


def happy_number(n_u_m: int) -> bool :
    """
    This function will search for lucky numbers if the number consists of less than 8 characters
    >>> happy_number(12345)
    False
    >>> happy_number(43211234)
    True
    >>> happy_number(191234)
    True
    >>> happy_number(0)
    True
    >>> happy_number(11111111111111)
    """
    n_u_m = str(n_u_m)
    left_slice, right_slice = 0, 0
    zero = 8 - len(n_u_m)
    n_u_m = zero * '0' + n_u_m
    if len(n_u_m) > 8 :
        return None
    for i in range(len(n_u_m)) :
        if 4 <= i < 8 :
            left_slice += int(n_u_m[i])
        if 0 <= i < 4 :
            right_slice += int(n_u_m[i])
    if left_slice == right_slice :
        return True
    if right_slice != left_slice :
        return False


def count_happy_numbers(n_1: int) -> int :
    """
    This function sorts lucky numbers
    """
    res = 0
    for i in range(1, n_1 + 1) :
        if happy_number(i) :
            res += 1
    return res

def happy_numbers(min_bottom: int, max_top: int) -> list :
    """
    This function searches for lucky numbers in the interval
    >>> happy_numbers(1, 3000)
    []
    >>> happy_numbers(100, 4000)
    []
    """
    result = []
    for i in range(min_bottom, max_top + 1) :
        if happy_number(i) :
            result.append(i)
    return result

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
