## input [1,2,3,4]
## output [24,12,8,6]


from typing import List


def product_arr_except_self(nums: List[int]):
    """
    Goes forward and then backward once
    """
    res = [1 for _ in range(len(nums))]
    prefix = 1
    postfix = 1
    for i in range(1, len(nums)):
        res[i] *= nums[i - 1] * prefix
        res[len(nums) - 1 - i] *= nums[len(nums) - i] * postfix
        prefix *= nums[i-1]
        postfix *= nums[len(nums) - i]

    return res


if __name__ == "__main__":
    print(product_arr_except_self([1, 2, 3, 4]))
