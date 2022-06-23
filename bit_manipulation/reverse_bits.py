# Reverse bits of a given 32 bits unsigned integer.


def reverse_bits(n: int) -> int:
    """
    (n >> i) & 1 = value of bit in i position
    << (31 - i) inverts the position of the bit

    m | ... puts the value on the left equal to the shifted bit
    """

    print(f"{n:b}")
    m = 0
    for i in range(32):
        m = m | (((n >> i) & 1) << (31 - i))

    print(f"{m:b}")
    return m


reverse_bits(20)
