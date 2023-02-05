# You are given a string s and an integer k.
# You can choose any character of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get
# after performing the above operations.

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

from collections import deque


def character_replacement(s: str, k: int) -> int:
    maxlen = 0
    for i in range(len(s)):
        if i + maxlen >= len(s):
            break
        j = i
        transform = 0
        extra_on_left = 0
        while transform <= k:
            j = j + 1
            if j >= len(s):
                extra_on_left = min(k - transform, i)
                break

            if s[j] != s[i]:
                transform = transform + 1

        curlen = j - i + extra_on_left
        if curlen > maxlen:
            maxlen = curlen
    return maxlen


def character_replacement_better(s: str, k: int) -> int:
    maxlen = 0
    for target in set(s):
        firstcharpos = deque([0])
        transform = 0
        for i in range(len(s)):
            if s[i] != target:
                firstcharpos.append(i + 1)
                if transform >= k:
                    maxlen = max(i - firstcharpos[0], maxlen)
                    firstcharpos.popleft()

                transform += 1
        maxlen = max(len(s) - firstcharpos[0], maxlen)
    return maxlen


def character_replacement_even_better(s: str, k: int) -> int:
    count = {}
    l = 0
    maxcount = 0
    maxlen = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        maxcount = max(maxcount, count[s[r]])
        if r - l - maxcount > k:
            count[s[l]] = count[s[l]] - 1
            l = l + 1
        maxlen = max(maxlen, r - l + 1)
    return maxlen


s = "AABABBA"
k = 1
print(character_replacement_even_better(s, k))
