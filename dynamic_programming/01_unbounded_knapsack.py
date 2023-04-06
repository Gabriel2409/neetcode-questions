# same as 0/1 knapsack but you can use an item several times


profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]
capacity = 8


def dfs_knapsack(
    index: int, profit: list[int], weight: list[int], capacity: int
) -> int:
    """
    Memory: O(2 ** capacity): at worst, in the decision tree, one element only costs
    1 capacity so we have a decision tree with two possibilities and the max height is
    the total capacity, not the number of elements
    Space: O(n)
    """

    if index == len(weight):
        return 0

    max_profit = dfs_knapsack(index + 1, profit, weight, capacity)

    if capacity - weight[index] >= 0:
        with_current = profit[index] + dfs_knapsack(
            index, profit, weight, capacity - weight[index]
        )
        # !only difference with 0/1 knapsack is here: when we call the dfs_knapsack function,
        # !we don't add 1 to the index
        max_profit = max(with_current, max_profit)
    return max_profit


def memo_knapsack(
    index: int, profit: list[int], weight: list[int], capacity: int
) -> int:
    """
    same as 0/1 knapsack
    Memory: O(n * capacity)
    Space: O(n * capacity)
    """

    cache = [[-1 for _ in range(capacity + 1)] for _ in range(len(weight))]

    if index == len(weight):
        return 0

    if cache[index][capacity] != -1:
        return cache[index][capacity]

    max_profit = memo_knapsack(index + 1, profit, weight, capacity)

    if capacity - weight[index] >= 0:
        with_current = profit[index] + memo_knapsack(
            index, profit, weight, capacity - weight[index]
        )
        # !only difference with 0/1 knapsack is here: when we call the memo_knapsack function
        # !we don't add 1 to the index
        max_profit = max(with_current, max_profit)
    cache[index][capacity] = max_profit
    return max_profit


def dp_knapsack(profit: list[int], weight: list[int], capacity: int) -> int:
    """
    same as 0/1 knapsack
    Memory: O(n * capacity)
    Space: O(n * capacity)
    """
    m = capacity
    n = len(profit)

    dp = [[0 for _ in range(m + 1)] for _ in range(n)]

    for cap in range(m + 1):
        if weight[0] <= cap:
            dp[0][cap] = profit[0]

    for i in range(1, n):
        for cap in range(1, m + 1):
            max_profit = dp[i - 1][cap]
            if cap - weight[i] >= 0:
                # ! diff with 0/1 knapsack : use element of current row instead of previous row
                with_current = profit[i] + dp[i][cap - weight[i]]
                max_profit = max(max_profit, with_current)
            dp[i][cap] = max_profit

    return dp[n - 1][m]


def min_dp_knapsack(profit: list[int], weight: list[int], capacity: int) -> int:
    """
    same as 0/1 knapsack
    Memory: O(n)
    Space: O(n)
    """
    m = capacity
    n = len(profit)

    # initialise only one row and fill it
    prev_row = [0 for _ in range(m + 1)]
    for cap in range(m + 1):
        if weight[0] <= cap:
            prev_row[cap] = profit[0]

    for i in range(1, n):
        cur_row = [0 for _ in range(m + 1)]
        for cap in range(1, m + 1):
            max_profit = prev_row[cap]
            if cap - weight[i] >= 0:
                # ! diff with 0/1 knapsack: use the current row
                with_current = profit[i] + cur_row[cap - weight[i]]
                max_profit = max(max_profit, with_current)
            cur_row[cap] = max_profit
        prev_row = cur_row

    return prev_row[m]


print(dfs_knapsack(0, profit, weight, capacity))
print(memo_knapsack(0, profit, weight, capacity))
print(dp_knapsack(profit, weight, capacity))
print(min_dp_knapsack(profit, weight, capacity))
