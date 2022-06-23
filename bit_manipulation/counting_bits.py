# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Input: n = 8
# Output: [0,1,1,2,1,2,2,3]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# 6 --> 110
# 7 --> 111
# 8 --> 1000


from typing import List


def counting_bits_hamming_looping(n: int) -> List[int]:
    """Basically just using the function in number_of_1_bits and looping on n"""
    arr = []
    for p in range(n + 1):
        count_one = 0
        while p:
            p = p & (p - 1)
            count_one += 1
        arr.append(count_one)
    return arr


def counting_bits(n: int):
    """Instead of counting every element independently, we can use the previous
    ones to infer the new nb of ones. Indeed, the pattern always repeat itself but
    with a 1 on the left
    """
    arr = [0] * (n + 1)
    offset = 1
    for i in range(1, n + 1):
        # when we arrive to the next 1 on the left, we move the offset
        if i == (offset << 1):
            offset = i
        arr[i] = 1 + arr[i - offset]
    return arr


if __name__ == "__main__":
    print(counting_bits_hamming_looping(16))
    print(counting_bits(16))
