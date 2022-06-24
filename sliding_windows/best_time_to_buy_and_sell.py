# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Input: prices = [7,1,5,3,6,4]
# Output: 5

# Input: prices = [7,6,4,3,1]
# Output: 0
from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Loop on the array, calculate potential profit at each day. Move the ref pointer
    each time you get a day with the lowest price.
    Time complexity: O(n)
    Space comp : O(1)
    """
    if not prices:
        return 0
    first_val = prices[0]
    max_profit = 0
    for curr in prices[1:]:

        if curr > first_val:
            max_profit = max(curr - first_val, max_profit)
        if curr < first_val:
            first_val = curr

    return max_profit


print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
