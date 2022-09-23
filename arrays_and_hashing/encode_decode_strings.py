from typing import List


def encode(strs: List[str]):
    """idea is to put str length with delimiter before string"""
    encoded = ""
    delimiter = ";"
    for str_ in strs:
        encoded += f"{len(str_)}{delimiter}{str_}"

    return encoded


def decode(encoded: str):
    delimiter = ";"
    if encoded == "":
        return []
    decoded: List[str] = []

    i = 0

    while i < len(encoded):
        j = i
        while encoded[j] != delimiter:
            j += 1
        length = int(encoded[i:j])

        decoded.append(encoded[j + 1 : j + 1 + length])
        i = j + 1 + length
    return decoded


mylist = ["lint", "45fdf;;;", ";4;4;;:dfd", ":dfdy$::;',]", "This is a long sentence"]


print(encode(mylist))
print(decode(encode(mylist)))
print(mylist == decode(encode(mylist)))
