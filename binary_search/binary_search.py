# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.


def bin_search(self, nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    if target == nums[l]:
        return l
    elif target == nums[r]:
        return r

    while l <= r :
        mid =   l + ((r - l) // 2) # avoid overflow

        if nums[mid] > target:
            r = mid -1
        elif nums[mid] < target:
            l = mid +1
        else:
            return mid
    return -1
