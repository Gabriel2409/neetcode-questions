# Given a string s, return the length of the longest palindrome of s

s = ["a", "b", "a", "a", "b"]


def pal(s):
    """start on a given char and expand right and left until cchar is different
    or we are out of bound. Must be performed for odd strings and even strings
    Memory: O(n^2)
    Space: O(n)
    """

    maxlen = 0
    for i in range(len(s)):
        # odd length palindromes
        l = i
        r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            maxlen = max(maxlen, r - l + 1)
            l = l - 1
            r = r + 1

        # even length palindromes
        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            maxlen = max(maxlen, r - l + 1)
            l = l - 1
            r = r + 1
    return maxlen
