# You are given an array of strings tokens that represents an arithmetic expression
#  in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6


def eval_rpn(tokens: list[str]) -> int:
    stack = []
    for el in tokens:
        if el in "+*-/":
            r = int(stack.pop())
            l = int(stack.pop())
            if el == "+":
                val = l + r
            elif el == "-":
                val = l - r
            elif el == "*":
                val = l * r
            elif el == "/":
                val = l / r
            stack.append(val)
        else:
            stack.append(el)

    return int(stack[-1])
