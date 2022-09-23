# Given a string s, find the length of the longest substring without repeating characters.


def length_of_longest_substring(s: str) -> int:
    longest = 0
    last_pos = 0

    char_set = set()
    for i in range(len(s)):
        if s[i] in char_set:
            curr_pos = i
            longest = max(longest, curr_pos - last_pos)
            last_pos = curr_pos
        char_set.add(s[i])

    longest = max(longest, len(s) - last_pos)

    return longest


if __name__ == "__main__":
    print(length_of_longest_substring("cdd"))
    print(length_of_longest_substring("abcabcbb"))
    print(length_of_longest_substring("dvdf"))
