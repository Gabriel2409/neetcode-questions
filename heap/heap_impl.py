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


def heapify(arr, i, max_ind=None):
    """Heapifies index i of array (subsequent indexes must already satisfy the heap property)"""
    if max_ind is None:
        max_ind = len(arr)

    right = 2 * i + 1
    left = 2 * i + 2
    largest = i
    if right < max_ind and arr[largest] < arr[right]:
        largest = right
    if left < max_ind and arr[largest] < arr[left]:
        largest = left

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, max_ind)


def max_heap(arr):
    """Applies heapify on all internal nodes"""
    i = len(arr) // 2 - 1

    while i >= 0:
        heapify(arr, i)
        i = i - 1

    return arr


def heapinsert(arr, num):
    """arr is a heap here"""
    arr.append(num)
    max_heap(arr)


def heapdelete(arr, num):
    """arr is a heap here"""
    arr[num], arr[len(arr) - 1] = arr[len(arr) - 1], arr[num]
    arr.pop()
    max_heap(arr)


def heap_sort(arr):
    final = deque()
    while arr:
        max_heap(arr)
        arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]
        final.appendleft(arr.pop())
    return final


def heap_sort_better(arr):
    # build max heap
    i = len(arr) // 2 - 1
    while i >= 0:
        heapify(arr, i)
        i = i - 1

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr


print(max_heap([3, 9, 2, 1, 4, 5]))
print(heap_sort([3, 9, 2, 1, 4, 5]))
print(heap_sort_better([3, 9, 2, 1, 4, 5]))
