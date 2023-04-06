# Given a list of N items and a backpack with limited capacity,
# return the max profit obtained from selecting items from the backpack
# profit and weight have same length (each element corresponds to weight
# / profit of a given item)


# construction of optimal method:
# 1 / basic dfs
# 2 / implement memoization to get cache size
# 3 / create dp solution with matrix of same size as cache and translate dfs operation 
# to lookup in dp matrix
# 4 / only keep relevant rows in memory


profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]
capacity = 8


def dfs_knapsack(
    index: int, profit: list[int], weight: list[int], capacity: int
) -> int:
    """
    basic dfs solution. For each element, we compare adding the current item and
    skipping it. Lots of repeated work
    Memory: O(2 ** n): height of the decision tree
    Space: O(n)
    """

    if index == len(weight):
        return 0

    # profit if we skip the current item
    max_profit = dfs_knapsack(index + 1, profit, weight, capacity)

    if capacity - weight[index] >= 0:
        # profit if we keep the current item
        with_current = profit[index] + dfs_knapsack(
            index + 1, profit, weight, capacity - weight[index]
        )
        max_profit = max(with_current, max_profit)
    return max_profit


def memo_knapsack(
    index: int, profit: list[int], weight: list[int], capacity: int
) -> int:
    """
    Same solution with memoization.
    We build a cache where rows are indices and columns are all possible capacities
    below chosen capacity
    Memory: O(n * capacity): Each element occurs at max once for a given capacity
    Space: O(n * capacity): size of the cache
    """

    # cache building
    cache = [[-1 for _ in range(capacity + 1)] for _ in range(len(weight))]

    if index == len(weight):
        return 0

    # return cached values
    if cache[index][capacity] != -1:
        return cache[index][capacity]

    max_profit = memo_knapsack(index + 1, profit, weight, capacity)

    if capacity - weight[index] >= 0:
        with_current = profit[index] + memo_knapsack(
            index + 1, profit, weight, capacity - weight[index]
        )
        max_profit = max(with_current, max_profit)
    # update cache
    cache[index][capacity] = max_profit
    return max_profit


def dp_knapsack(profit: list[int], weight: list[int], capacity: int) -> int:
    """
    dynamic programming solution, same size as solution with cache
    Memory: O(n * capacity): Each element occurs at max once for a given capacity
    Space: O(n * capacity): size of the dp matrix
    """
    m = capacity
    n = len(profit)

    # initialise dp matrix: rows for index and columns for capacities, same as cache
    dp = [[0 for _ in range(m + 1)] for _ in range(n)]

    # filling first row to avoid edge cases
    for cap in range(m + 1):
        if weight[0] <= cap:
            dp[0][cap] = profit[0]

    # starting from second row
    for i in range(1, n):
        for cap in range(1, m + 1):
            # previous profit (without current item)
            max_profit = dp[i - 1][cap]
            if cap - weight[i] >= 0:
                # profit with current item. Add current profit to profit of all 
                # previous items after removing the capacity of current item
                with_current = profit[i] + dp[i - 1][cap - weight[i]]
                max_profit = max(max_profit, with_current)
            # fill the current profit for given index and cap
            dp[i][cap] = max_profit

    # last element of the matrix
    return dp[n - 1][m]


def min_dp_knapsack(profit: list[int], weight: list[int], capacity: int) -> int:
    """
    dynamic programming solution,while only keeping the previous row in memory.
    Memory: O(n): Each element occurs at max once for a given capacity
    Space: O(n): size of the cache
    """
    m = capacity
    n = len(profit)

    # initialise only one row and fill it
    prev_row = [0 for _ in range(m+1)]
    for cap in range(m + 1):
        if weight[0] <= cap:
            prev_row[cap] = profit[0]

    for i in range(1, n):
        cur_row = [0 for _ in range(m+1)]
        for cap in range(1, m + 1):
            max_profit = prev_row[cap]
            if cap - weight[i] >= 0:
                with_current = profit[i] + prev_row[cap - weight[i]]
                max_profit = max(max_profit, with_current)
            cur_row[cap] = max_profit
        prev_row = cur_row

    return prev_row[m]


# print(dfs_knapsack(0, profit, weight, capacity))
# print(memo_knapsack(0, profit, weight, capacity))
# print(dp_knapsack(profit, weight, capacity))
print(min_dp_knapsack(profit, weight, capacity))
