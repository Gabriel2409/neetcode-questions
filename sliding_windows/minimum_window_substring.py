# Given two strings s and t of lengths m and n respectively, return the minimum window
# substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


def min_window(s: str, t: str) -> str:
    smallest = ""

    def is_complete(t_count, s_count):
        for key, val in t_count.items():
            if val > s_count.get(key, 0):
                return False
        return True

    t_count = {}
    for chr_ in t:
        t_count[chr_] = t_count.get(chr_, 0) + 1
    l = 0

    s_count = {}
    for r in range(len(s)):
        if s[r] in t_count:
            s_count[s[r]] = s_count.get(s[r], 0) + 1
            if s_count[s[r]]  >= t_count[s[r]]:
                if is_complete(t_count, s_count):
                    while l < r:
                        if s[l] not in t_count:
                            l = l + 1
                        else:
                            if s_count[s[l]] == t_count[s[l]]:
                                break
                            s_count[s[l]] = s_count[s[l]] - 1
                            l = l + 1
                    if smallest == "" or len(smallest) > r - l:
                        smallest = s[l : r + 1]

    return smallest

print(min_window("ADOBECODEBANC", "ABC"))