# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. ->length is 4.
import random
from typing import List


# this is O(n) complexity as we remove elements from the dict
def longest_consecutive(nums: List[int]) -> int:

    # total_ops = 0
    if not nums:
        return 0 
    maxlen = 1
    a = {num:1 for num in nums}

    for el in nums:
        # total_ops +=1
        if el not in a:
            continue
        b = el
        while (b + 1) in a:
            # total_ops +=1
            b = b + 1
            a[el] = a[el] + a[b]
            del a[b]
            if a[el] > maxlen:
                maxlen = a[el]
    # print(total_ops)
    return maxlen

def longest_consecutive_better(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    total_ops = 0
    for n in nums:
        total_ops +=1
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                total_ops +=1
                length += 1
            longest = max(length, longest)
    print(total_ops)
    return longest


# nums = [100, 4, 200, 1, 3, 2]
nums  =  random.sample(range(1,1000000),45000)
print(longest_consecutive(nums))
