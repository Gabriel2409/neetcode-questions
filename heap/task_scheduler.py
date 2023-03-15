# Given a characters array tasks, representing the tasks a CPU needs to do,
# where each letter represents a different task. Tasks could be done in any order.
# Each task is done in one unit of time. For each unit of time, the CPU could complete
# either one task or just be idle.

# However, there is a non-negative integer n that represents
# the cooldown period between two same tasks (the same letter in the array),
# that is that there must be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all
# the given tasks.

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.
from collections import Counter, deque
import heapq


def least_interval(tasks: list[str], n: int) -> int:
    counter = Counter(tasks)
    # count occurences of each task
    max_heap = [-c for c in counter.values()]
    # most frequent task to pop first
    heapq.heapify(max_heap)

    time = 0
    q = deque()
    while max_heap or q:
        time += 1

        if max_heap:
            # pop last element 
            c = 1 + heapq.heappop(max_heap)
            # append to queue if there are still identical tasks to perform 
            if c:
                q.append((c, time + n))
        # if we popped everything, all the times are in the queue so we restart from the first el of the queue
        else:
            time = q[0][1]
        

        if q and q[0][1] == time:
            heapq.heappush(max_heap, q.popleft()[0])

    return time


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(least_interval(tasks, n))
