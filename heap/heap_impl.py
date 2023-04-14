# heap data structure implementation
# maxheap: Each node is always greater than its child node/s and the key of the root
# node is the largest among all other nodes.

# minheap: Each node isalways smaller than the child node/s and the key of
# the root node is the smallest among all other nodes
# NOTE: python implements a minheap

# To heapify an array, we first create a complete binary tree from it and then
# heapify the tree, which means recursively swapping until heap property is satisfied

# [3,9,2,1,4,5] becomes
#         3
#    9         2
#  1  4       5
# which means the leaves indexes  are from len(arr) // 2 to the len(arr) -1
# heapify 2 => swap 2 and 5,
# heapify 9 => nothing happens
# heapify 3 => swap 9 and 3 then swap 3 and 4
#         9
#    4         5
#  1  3       2
# final is [9,4,5,1,3,2]. Now root node is the max
from collections import deque


def percolate_down(arr, i, limit=None):
    """nodes at subsequent indexes are supposed to already satisfy the order property"""

    if limit is None:
        limit = len(arr)
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    if left < limit and arr[left] < arr[smallest]:
        smallest = left
    if right < limit and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        percolate_down(arr, smallest, limit)


def percolate_down_iterative(arr, i):
    while 2 * i + 1 <= len(arr):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(arr) and arr[left] < arr[smallest]:
            smallest = left
        if right < len(arr) and arr[right] < arr[smallest]:
            smallest = right
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
        else:
            break


def percolate_up(arr, i):
    """nodes at previous indexes are supposed to already satisfy the order property"""
    parent = (i + 1) // 2 - 1
    if parent >= 0 and arr[parent] > arr[i]:
        arr[parent], arr[i] = arr[i], arr[parent]
        percolate_up(arr, parent)


def percolate_up_iterative(arr, i):
    while i > 0:
        parent = (i + 1) // 2 - 1
        if arr[parent] > arr[i]:
            arr[parent], arr[i] = arr[i], arr[parent]
        else:
            break


def heapify(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        percolate_down(arr, i)


def hpop(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
    val = arr.pop()
    percolate_down(arr, 0)
    return val


def hpush(arr, val):
    arr.append(val)
    percolate_up(arr, len(arr) - 1)


arr = [4, 3, 1, 8, 7, 6, 2, 4, 5, 8, 3, 1, 5, 8]
heapify(arr)
print(arr)
hpush(arr, 0)
hpush(arr, 6)
hpush(arr, 3)
hpush(arr, 3)
while arr:
    val = hpop(arr)
    print(val)


def heap_sort(arr):
    heapify(arr)
    for i in range(len(arr)):
        percolate_down(arr, 0, limit=len(arr) - i)
        arr[0], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[0]
    return arr

print(heap_sort([1,2,5,8,74,5,6,321,8,5,2,7,5,1,8,75,23,8,5,7,8,94,1,5,74,0,3,2]))
