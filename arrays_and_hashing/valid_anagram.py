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

    counter = {}
    for el in s:
        counter[el] = counter.get(el, 0) + 1
    for el in t:
        counter[el] = counter.get(el, 0) - 1

    for key, val in counter.items():
        if val != 0:
            return False
        return True
