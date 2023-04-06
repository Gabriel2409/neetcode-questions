# Given two strings s1 and s2, find the length of longest common subsequence between the
# two strings.
# s1 = "abcd"
# s2 = "aec"
# result = "ac"
from typing import Optional

s1 = "adcb"
s2 = "abc"


def dfs_lcs(s1: str, s2: str, i1: int, i2: int) -> int:
    """
    Basic dfs solution. Have two pointers starting on the beginning of each string and
    move them right either at the same time if char is equal or one at a time
    n = len(s1), m = len(s2)
    Memory: O(2 ^ (n+m)) = size of binary decision tree
    Space = O(n+m)

    """
    if i1 == len(s1) or i2 == len(s2):
        return 0

    if s1[i1] == s2[i2]:
        # same char, add it to the sequence and move pointers left
        return 1 + dfs_lcs(s1, s2, i1 + 1, i2 + 1)
    else:
        # different char, try to move one pointer ahead
        return max(dfs_lcs(s1, s2, i1 + 1, i2), dfs_lcs(s1, s2, i1, i2 + 1))


def memo_lcs(s1: str, s2: str, i1: int, i2: int, cache: Optional[list] = None) -> int:
    """
    same solution with caching (memoization)
    Memory: O(n*m) = size of all the combinations
    Space = O(n*m) = size of the cache
    """

    if i1 == len(s1) or i2 == len(s2):
        return 0

    n = len(s1)
    m = len(s2)

    if not cache:
        cache = [[-1 for _ in range(m)] for _ in range(n)]

    if cache[i1][i2] != -1:
        return cache[i1][i2]

    if s1[i1] == s2[i2]:
        cache[i1][i2] = 1 + dfs_lcs(s1, s2, i1 + 1, i2 + 1)
    else:
        cache[i1][i2] = max(dfs_lcs(s1, s2, i1 + 1, i2), dfs_lcs(s1, s2, i1, i2 + 1))
    return cache[i1][i2]


def dp_lcs(s1: str, s2: str) -> int:
    """
    dynamic programming solution.
    Note: alternatively, instead of filling first row and col, it is possible to add
    an extra row and an extra col filled with 0
    Memory: O(n*m) = go through all the combinations
    Space = O(n*m) = size of the dp matrix
    """
    n = len(s1)
    m = len(s2)

    dp = [[0 for _ in range(m)] for _ in range(n)]

    # fill first row
    for i2 in range(m):
        if s1[0] == s2[i2]:
            dp[0][i2] = 1
    # fill first col
    for i1 in range(n):
        if s2[0] == s1[i1]:
            dp[i1][0] = 1

    for i1 in range(1, n):
        for i2 in range(1, m):
            if s1[i1 - 1] == s2[i2 - 1]:
                dp[i1][i2] = 1 + dp[i1 - 1][i2 - 1]

            else:
                dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])

    return dp[n - 1][m - 1]


def min_dp_lcs(s1: str, s2: str) -> int:
    """
    same as dynamic programming solution but while keeping only last row in cache.
    Also used alternative mentionned in dp_lcs
    Memory: O(n*m) = go through all the combinations
    Space = O(m) = size of the dp matrix
    """
    n = len(s1)
    m = len(s2)

    prev_row = [0 for _ in range(m + 1)]

    for i1 in range(n):
        cur_row = [0 for _ in range(m + 1)]
        for i2 in range(m):
            if s1[i1] == s2[i2]:
                cur_row[i2 + 1] = 1 + prev_row[i2]
            else:
                cur_row[i2 + 1] = max(prev_row[i2 + 1], cur_row[i2])
        prev_row = cur_row

    return cur_row[m]


print(dfs_lcs(s1, s2, 0, 0))
print(memo_lcs(s1, s2, 0, 0))
print(dp_lcs(s1, s2))
print(min_dp_lcs(s1, s2))
