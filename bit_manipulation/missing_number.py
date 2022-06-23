# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
from typing import List


def missing_number_arithmetic_sum(nums: List[int]) -> int:
    """with arithmetic sum"""
    n = len(nums)
    return (n * (n + 1) // 2) - sum(nums)


def missing_number(nums: List[int]) -> int:
    """Even better, only need to loop once"""
    res = len(nums)
    for i, el in enumerate(nums):
        res = res + i - el

    return res


print(missing_number([0, 1, 2, 4]))
