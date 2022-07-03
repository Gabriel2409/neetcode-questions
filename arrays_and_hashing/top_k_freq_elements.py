# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

from typing import List


def top_k(nums: List[int], k: int) -> List[int]:
    """
    Idea create a array of size n.
    Maintain a counter to always know the nb of occurence of an element.
    Add given element to corresponding index in array. Loop in reverse and
    only count a digit if it is in the valid index
    """
    n = len(nums)
    max_count = 0
    arr = [[] for i in range(n)]

    el_counter = {}
    final = []

    for el in nums:
        if el in el_counter:
            val = el_counter[el] + 1
        else:
            val = 1
        el_counter[el] = val
        if val > max_count:
            max_count = val

        arr[val - 1].append(el)

    nb_added = 0
    for i in range(max_count - 1, -1, -1):
        for el in arr[i]:
            if el_counter[el] == i + 1:
                final.append(el)
                nb_added += 1
                if nb_added == k:
                    return final


if __name__ == "__main__":
    print(top_k([1, 2, 1, 3, 1, 2, 4], 2))
