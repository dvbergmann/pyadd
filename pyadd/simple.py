from numbers import Number


def add_int(a: int, b: int) -> int:
    """
    returns the addition of two integers a and b
    :param a: integer to add
    :param b: integer to add
    :return: the sum of the integers
    """

    return a + b


def add(a: Number, b: Number) -> Number:
    """
    returns the addition of two numbers a and b
    :param a: number to add
    :param b: number to add
    :return: the sum of the numbers
    """

    return a + b


def multiple_add(*nums) -> Number:
    """
    Returns the sum of the given numbers

    :param nums: multiple numbers
    :return: the sum of nums
    """

    return sum(nums)
