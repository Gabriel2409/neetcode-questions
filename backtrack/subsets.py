# Given an integer array nums of unique elements, return all possible
# subsets
# (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
from copy import deepcopy


def subsets(nums: list[int]) -> list[list[int]]:
    if not nums:
        return [[]]

    if len(nums) == 1:
        return [[], [nums[0]]]

    final = []

    sub1 = subsets(nums[1:])
    final.extend(sub1)

    sub2 = deepcopy(sub1)
    for el in sub2:
        el.append(nums[0])

    final.extend(sub2)

    return final


print(subsets([1, 2, 3, 4]))
