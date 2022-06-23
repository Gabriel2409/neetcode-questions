# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).


def hamming_weight_switch(n: int) -> int:
    """
    switch by one until there is no more 1 in n
    """
    print(f"{n:b}")
    count_one = 0
    while n:
        if n & 1:
            count_one += 1
        n = n >> 1
    return count_one


def hamming_weight(n: int) -> int:
    """
    Even faster
    Ex: n = 1001 => n-1 = 1000,
    n & (n-1) = 1000
    next pass: n & (n-1) = 0
    Finished in 2 passes
    """
    print(f"{n:b}")
    count_one = 0
    while n:
        n = n & (n - 1)
        count_one += 1
    return count_one


if __name__ == "__main__":
    print(hamming_weight(5))
    print(hamming_weight(15))
    print(hamming_weight(157))
