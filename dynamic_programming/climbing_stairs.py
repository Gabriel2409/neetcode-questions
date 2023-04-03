# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
from functools import lru_cache


@lru_cache
def climbing_stairs_recursive(n: int):
    """
    If we have the combinations of n-2 and n-1, we can get all the
    combinations by appending 2 to the n-2 combs and 1 to the n-1 combs.

    Needs lru_cache to keep previous results

    Time complexity: O(n) because of caching
    Space complexity: O(n)
    """

    if n <= 2:
        return n

    return climbing_stairs(n - 1) + climbing_stairs(n - 2)


def climbing_stairs(n: int):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """

    if n <= 2:
        return n
    n1, n2 = 1, 2
    for i in range(3, n + 1):
        next_nb = n1 + n2
        n1 = n2
        n2 = next_nb

    return n2


if __name__ == "__main__":

    print(climbing_stairs(3))
    print(climbing_stairs(4))
    print(climbing_stairs(5))
    print(climbing_stairs(6))
    print(climbing_stairs(38))
