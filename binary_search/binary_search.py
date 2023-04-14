# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

def binary_search(arr: list[int], target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2  # avoids overflow, equivalent to (l+r)//2

        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1


def binary_search_rec(arr, target):
    return helper(arr, 0, len(arr), target)

def helper(arr, l, r, target):
    if l == r:
        return -1
    mid = (l + r) // 2
    if arr[mid] < target:
        return helper(arr, mid + 1, r, target)
    elif arr[mid] > target:
        return helper(arr, l, mid, target)
    else:
        return mid


print(binary_search_rec([1, 3, 5, 8, 12, 19], 22))

