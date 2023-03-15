# Given an array of integers heights representing the histogram's bar height where the 
# width of each bar is 1, return the area of the largest rectangle in the histogram.
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

def largest_rectangle_area(heights: list[int]) -> int:

    max_area = 0
    stack = []

    heights.append(0)


    for height in heights:
        width = 0
        while stack and height <= stack[-1][0]:
            h,w = stack.pop()
            width = width + w 
            max_area = max(h * width, max_area)

        stack.append((height, width+1))
  

    return max_area

print(largest_rectangle_area([2,1,5,6,2,3]))