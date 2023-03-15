# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").


def check_inclusion(s1: str, s2: str) -> bool:
    n = len(s1)
    count = {}
    for el in s1:
        count[el] = count.get(el, 0) + 1

    l = 0
    added = 0
    cc = {}
    for r in range(len(s2)):
        if s2[r] not in count:
            added = 0
            cc = {}
            l = r + 1
            continue

        if cc.get(s2[r], 0) + 1 > count[s2[r]]:
            while s2[l] != s2[r]:
                added = added - 1

                cc[s2[l]] = cc[s2[l]] - 1
                l = l + 1
            cc[s2[l]] = cc[s2[l]] - 1
            added = added - 1
            l = l + 1

        added = added + 1
        cc[s2[r]] = cc.get(s2[r], 0) + 1
        if added == n:
            return True
    return False

s1 = "abac"

s2 = "eidabbbbbbbbbbbbbbbbbbbc"

print(check_inclusion(s1,s2))