# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

from typing import List


def three_sum(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    if n < 3:
        return []

    # triplets = []
    #
    # for i in range(n - 2):
    #     for j in range(i + 1, n - 1):
    #         for k in range(j + 1, n):
    #             if nums[i] + nums[j] + nums[k] == 0:
    #                 triplets.append([i, j, k])
    #
    # return triplets
