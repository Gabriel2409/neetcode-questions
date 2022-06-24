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
    print(f"Perf for n={n}", b - a)
    return res


if __name__ == "__main__":
    # print(generate_parenthesis(1))
    # print(generate_parenthesis(2))
    print(generate_parenthesis(3))
    # print(generate_parenthesis(4))
    for i in range(20):
        generate_parenthesis(i)
