# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
import random
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    counter = {}
    final = []
    # creates a counter
    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    already_processed = set()
    tot = 0
    for i in range(len(nums)):

        tot += 1
        if nums[i] in already_processed:
            continue

        processed_in_current = set()
        for j in range(i + 1, len(counter)):
            tot += 1
            if nums[j] in already_processed or nums[j] in processed_in_current:
                continue

            target = -nums[i] - nums[j]
            if target in already_processed or target in processed_in_current:
                continue

            value_to_beat = 0
            if nums[j] == nums[i]:
                value_to_beat += 1
            if nums[j] == target or nums[i] == target:
                value_to_beat += 1

            if counter.get(target, 0) > value_to_beat:
                final.append([nums[i], nums[j], target])
                processed_in_current.add(nums[j])
                processed_in_current.add(target)
        already_processed.add(nums[i])

    print(tot)
    return final


# print(three_sum([-1, 0, 1, 2, -1, -4]))
n= 90
three_sum(random.sample(range(-2500, 2500), n))
print(n*(n+1)/2)
