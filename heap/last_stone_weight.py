# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones.
# On each turn, we choose the heaviest two stones and smash them together.
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

#     If x == y, both stones are destroyed, and
#     If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
import heapq


def last_stone_weight(stones: list[int]) -> int:
    stones = [a * -1 for a in stones]
    heapq.heapify(stones)

    while len(stones) >= 2:
        a = heapq.heappop(stones)
        b = heapq.heappop(stones)
        if a != b:
            heapq.heappush(stones, a - b)

    if stones:
        return stones[0] * -1
    else:
        return 0
    
print(last_stone_weight([1,3]))
