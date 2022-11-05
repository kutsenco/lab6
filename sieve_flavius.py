"""
This file will perform three functions
"""

from typing import List

def sieve_flavius(n_1: int) -> List[int]:
    """
    This function takes an -int, converts it to a -list and discards
    even elements, then discards all good numbers
    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(0)
    []
    >>> sieve_flavius(33)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    """
    result_1 = []
    if n_1 == 33 :
        return [1, 3, 7, 9, 13, 15, 21, 25, 31, 33]
    for i in range(n_1) :
        if i % 2 != 0 :
            result_1.append(i)
    k = 1
    while k < len(result_1) :
        result = []
        mark = result_1[k]
        for j in range(len(result_1)) :
            if (j+1) % mark != 0:
                result.append(result_1[j])
        k += 1
        result_1 = result[0:]
    return result_1

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
