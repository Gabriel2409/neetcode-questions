# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.


def is_valid(s: str) -> bool:
    """
    time comp: O(n)
    Space comp: O(1)
    """
    matches = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    stack = []
    try:
        for c in s:
            if c in matches:
                popped = stack.pop()
                if not popped == matches[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
    except IndexError:
        return False


if __name__ == "__main__":
    print(is_valid("()"))
    print(is_valid("([]{[()]})"))
    print(is_valid("([)]{"))
