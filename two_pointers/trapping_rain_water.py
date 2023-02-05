# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
from typing import List
# trick is to divide into 2 parts so that the last element of the list is always the 
# highest
def trap(height: List[int]) -> int:


    max_height = 0
    max_index = 0
    for i,el in enumerate(height):
        if el > max_height:
            max_height = el
            max_index = i

    left_height = height[:max_index +1] 
    right_height = height[max_index:]


    cur_area = 0
    cur_height = 0
    for el in left_height:
        if el < cur_height:
            cur_area = cur_area + cur_height - el
        else:
            cur_height = el

    cur_height = 0
    for el in right_height[::-1]:
        if el < cur_height:
            cur_area = cur_area + cur_height - el
        else:
            cur_height = el
    return cur_area 

height = [2,0,2]
print(trap(height))