# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
#
#     MinStack() initializes the stack object.
#     void push(int val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.


class MinStack:
    """stack and min stack have diff sizes"""

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class MinStackEvenEasier:
    """stack and min stack have same size"""

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            appended_val = val
        else:
            appended_val = min(self.min_stack[-1], val)
        self.min_stack.append(appended_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
