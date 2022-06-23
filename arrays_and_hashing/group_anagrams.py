# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from typing import List


def group_anagrams_sort_str(strs: List[str]) -> List[List[str]]:
    """Loops only once through everything
    but needs to sort each string
    N element, avg str length P => Time complexity at least O(NPlogP), space comp:
    depends on sorting
    """
    full_dict = {}
    for str_ in strs:
        sorted_str = "".join(sorted(str_))
        if sorted_str not in full_dict:
            full_dict[sorted_str] = []
        full_dict[sorted_str].append(str_)

    return list(full_dict.values())


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Loops only once through everything and stores counts in a
    list. Only works with lowercase words with no special chars

    N element, avg str len P => time comp = O(NP), space comp (list of 26 els) = O(1)
    """

    full_dict = {}
    for str_ in strs:
        list_of_letters = [0] * 26
        for letter in str_:
            list_of_letters[ord(letter) - ord("a")] += 1
        dict_key = tuple(list_of_letters)
        if dict_key not in full_dict:
            full_dict[dict_key] = []
        full_dict[dict_key].append(str_)

    return list(full_dict.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
