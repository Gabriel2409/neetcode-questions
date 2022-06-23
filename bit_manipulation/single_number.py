# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

from typing import List


def single_number(nums: List[int]):
    """Space complexity O(1), time complexity O(n)"""
    val = 0
    for num in nums:
        val = val ^ num

    return val


if __name__ == "__main__":
    print(single_number([1, 1, 2, 3, 4, 2, 4]))
