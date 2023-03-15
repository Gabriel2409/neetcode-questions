# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
from time import perf_counter
from typing import List


def generate_parenthesis(n: int) -> List[str]:
    """

    Complexity ? I think it is exponential in n
    Insert open bracket in priority.
    Each time i add (, i check if i can add another ( in priority, then a ) then pop
    Each time i add a ), i check if I can add a ( in priority then ( then pop
    Each time I pop a (, I check if I can add a ) in priority else pop
    Each time I pop a ), I keep popping

    n = 2
    ( -> (( -> (() ->
    (()) -> (() -> (( -> ( -> () -> ()( ->
    ()() -> ()( -> () -> ( ->


    n = 3
    ( -> (( -> ((( -> ((() -> ((()) ->
    ((())) -> ((()) -> ((() -> ((( -> (( -> (() -> (()( -> (()() ->
    (()()) -> (()() -> (()( -> (() -> (()) -> (())( ->
    (())() -> (())( -> (()) -> (() -> (( -> ( -> () -> ()( -> ()(( -> ()(() ->
    ()(()) -> ()(() -> ()(( -> ()( -> ()() -> ()()( ->
    ()()() -> ()()( -> ()() -> ()( -> () -> ( ->
    """

    def populate(opened: int, closed: int):
        if opened == closed == n:
            res.append("".join(stack))

        if opened < n:
            stack.append("(")
            populate(opened + 1, closed)
            stack.pop()

        if closed < opened:
            stack.append(")")
            populate(opened, closed + 1)
            stack.pop()

    a = perf_counter()
    stack = []
    res = []
    populate(0, 0)
    b = perf_counter()
    print(f"Recursive Perf for n={n}", b - a)
    return res


def generate_parenthesis_iterative(n: int) -> list[str]:
    a = perf_counter()
    output:list[str] = []
    cur = []
    l = 0
    r = 0
    if n == 0:
        return []
    while True:
        while l < n:
            cur.append("(")
            l = l + 1
        while r < n:
            cur.append(")")
            r = r + 1

        output.append("".join(cur))
        while cur:
            if l == 1:
                b = perf_counter()
                print(f"Iterative Perf for n={n}", b - a)
                return output
            val = cur.pop()
            if val == ")":
                r = r - 1
            else:
                l = l - 1
                if r < l:
                    cur.append(")")
                    r = r + 1
                    break


if __name__ == "__main__":
    # print(generate_parenthesis(1))
    # print(generate_parenthesis(2))
    # print(generate_parenthesis(3))
    # print(generate_parenthesis(4))
    for i in range(20):
        generate_parenthesis(i)
        generate_parenthesis_iterative(i)
    # print(generate_parenthesis_iterative(3))
