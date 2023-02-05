# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49


from typing import List


def max_area(height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    max_area = min(height[l], height[r]) * (r - l)

    while l < r:
        j = 0
        if height[l] <= height[r]:
            while height[l + j] <= height[l]:
                j = j + 1
                if l + j == r:
                    return max_area
            l = l + j
            area = min(height[l], height[r]) * (r - l)
            if area > max_area:
                max_area = area
        else:
            while height[r - j] <= height[r]:
                j = j + 1
                if r - j == l:
                    return max_area
            r = r - j
            area = min(height[l], height[r]) * (r - l)
            if area > max_area:
                max_area = area
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))
