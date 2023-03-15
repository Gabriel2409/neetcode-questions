# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
#  For example, the array nums = [0,1,2,4,5,6,7] might become:

#     [4,5,6,7,0,1,2] if it was rotated 4 times.
#     [0,1,2,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements,
# return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.


def find_min_rotated_array(nums: list[int]) -> int:
    l = 0
    r = len(nums) - 1
    mid = 0
    while l <= r-1:
        mid = (l + r) // 2

        if nums[mid] > nums[r]:
            mid = mid + 1
            l = mid
        else:
            r = mid

    return nums[mid]

nums = [2,1]
print(find_min_rotated_array(nums))