# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    """
    loops only once.
    Needs extra memory.
    Time comp O(n)
    Space comp O(n)
    """
    n = len(cost)
    if n < 1:
        return 0
    prev_cost = [0] * n

    for i in range(2, n):
        prev_cost[i] = min(
            prev_cost[i - 1] + cost[i - 1], prev_cost[i - 2] + cost[i - 2]
        )

    return min(prev_cost[n - 1] + cost[n - 1], prev_cost[n - 2] + cost[n - 2])


def min_cost_climbing_stairs_no_extra_memory(cost: List[int]) -> int:
    """
    loops only once.
    Needs extra memory.
    Time comp O(n)
    Space comp O(1) but modifies cost array
    """
    n = len(cost)
    if n < 1:
        return 0

    for i in range(2, n):
        cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])

    return min(cost[n - 1], cost[n - 2])


if __name__ == "__main__":
    print(min_cost_climbing_stairs([10, 15, 20]))
    print(min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
