# outputs true if two inputs are anagrams


def is_anagram_with_sort(s: str, t: str):
    """sorting is O(nlogn)
    => time complexity: O(nlogn)
    space complexity: depends on sort algo

    """
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)


def is_anagram_with_counter(s: str, t: str):
    """Instead of using Counter, i manually construct it
    time complexity O(n)
    space complexity O(n)
    """
    if len(s) != len(t):
        return False
    s_dict = {}
    t_dict = {}
    for a, b in zip(s, t):
        s_dict[a] = s_dict.get(a, 0) + 1
        t_dict[b] = t_dict.get(b, 0) + 1

    return t_dict == s_dict
