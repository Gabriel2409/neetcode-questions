# A phrase is a palindrome if, after converting all uppercase letters into lowercase
# letters and removing all non-alphanumeric characters, it reads the same forward and
# backward. Alphanumeric characters include letters and numbers.


def is_palindrome(s: str) -> bool:
    """
    TIme comp: O(n)
    Space comp: O(1)
    could write own alphanum, just use ord("a")< ord(c) < ord("z"), etc...
    """
    i = 0
    j = len(s) - 1

    s = s.lower()
    while i < j:
        while not s[i].isalnum():
            i = i + 1

        while not s[j].isalnum():
            j = j - 1

        if s[i] != s[j]:
            return False
        i = i + 1
        j = j - 1
    return True


if __name__ == "__main__":
    print(is_palindrome(""))
    print(is_palindrome("ab  cd cbA"))
    print(is_palindrome("abcddcba"))
    print(is_palindrome("abdsdcddcba"))
