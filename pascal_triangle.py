"""
Pascal's triangle
"""

def generate_pascal_triangle(rows: int) -> list :
    """
    this file will generate Pascal's triangle when
    the -int value is entered into the function (-int)
    >>> generate_pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> generate_pascal_triangle(-5)
    []
    >>> generate_pascal_triangle(0)
    []
    """
    if not isinstance(rows, int) :          
        return None
    if rows == 0 :
        return []
    if rows <= 0 :
        return []
    result = [[1]]
    row = [1]
    for _ in range(rows - 1) :
        row = [sum(x) for x in zip([0]+row, row+[0])]
        result.append(row)
    return result

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
