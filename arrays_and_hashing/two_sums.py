# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
# assume unique solution. DO not use same element twice

from typing import List


def two_sum_double_for_loop(nums: List[int], target: int) -> List[int]:
    """Time complexity: O(n2)
    Space complexity O(1)

    Brute force looping


    """
    for i, n1 in enumerate(nums):
        for j, n2 in enumerate(nums[i + 1 :], i + 1):
            if (n1 + n2) == target:
                return [i, j]


def two_sum_add_target(nums: List[int], target: int) -> List[int]:
    """
    Time complexity: O(n)
    Space complexity O(n)

    While looping, reate a dict storing value and index of first element.
    Then, if target - current el is in the dict, you found the second element and
    can deduce the index of the first with the dict
    """
    val_dict = {}
    for i, el in enumerate(nums):
        if target - el in val_dict:
            return [val_dict[target - el], i]
        if el not in val_dict:
            # ensures to use first index on the most left part
            val_dict[el] = i


if __name__ == "__main__":
    print(two_sum_add_target([3, 2, 4], 6))
    print(two_sum_add_target([1, 2, 1, 4], 5))
    print(two_sum_add_target([1, 2, 1, 2], 4))
