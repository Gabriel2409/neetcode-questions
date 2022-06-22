# Returns true if array contains duplicates
from typing import List


def contains_duplicates_double_for_loop(nums: List[int]):
    """Time comp O(n2)
    Space com O(1)
    """
    for i, num in enumerate(nums):
        for n2 in nums[i + 1 :]:
            if n2 == num:
                return True
    return False


# note: we can also sort the array and then we only have to go through it once and
# compare adjascent neighbors


def contains_duplicates_set(nums: List[int]):
    """Time comp O(n), Space comp O(n)"""
    hashset = set()
    for num in nums:
        if num in set:
            return True
        hashset.add(num)
    return False
