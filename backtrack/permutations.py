# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


def permute(nums: list[int]) -> list[list[int]]:
    def dfs(i):
        if i >= len(nums):
            return [[]]

        combs = dfs(i + 1)
        final = []
        for comb in combs:
            newcombs = [comb[:j] + [nums[i]] + comb[j:] for j in range(1+len(comb))]
            final.extend(newcombs)
        return final

    return dfs(0)


print(permute([1,2,3,4]))


