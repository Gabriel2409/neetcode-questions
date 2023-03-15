
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown 
# pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], 
# ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] 
# might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
def binsearch_rotated(nums: list[int], target: int) -> int:

    l = 0
    r = len(nums) - 1

    while l <= r:
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid

        if nums[r] >= nums[l]:
            if target > nums[mid]:
                l = mid +1
            else:
                r = mid - 1
        else:
            if nums[mid] > nums[r]:
                # reset between mid and r
                if nums[mid] < target:
                    l = mid + 1
                else:
                    if nums[r] < target:
                        r = mid -1
                    else:
                        l = mid + 1
                    
            elif nums[mid] < nums[l]:
                # reset between l and mid
                if nums[mid] > target:
                    r = mid - 1
                else:
                    if nums[l] > target:
                        l = mid + 1
                    else:
                        r = mid - 1
            else:
                raise ValueError("Not possible")
            
        
            

    return -1


nums = [4,5,6,7,8,1,2,3]
target = 8
# nums = [4,5,6,7,0,1,2]
# target = 0
nums = [8,1,2,3,4,5,6,7]
target = 6
nums = [4,5,6,7,0,1,2]
target = 5
print(binsearch_rotated(nums,target))