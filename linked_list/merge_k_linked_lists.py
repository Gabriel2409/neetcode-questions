# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next
    def __repr__(self):
        if self.next:
            next_val = self.next.val
        else:
            next_val = None
        return f"{self.val}->{next_val}"

def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:

    def get_min_node(lists): 
        minnode = None
        minind = None
        for i,n in enumerate(lists):
            if n is None:
                continue
            if minnode is None or n.val < minnode.val:
                minnode = n
                minind = i
        if minnode: 
            lists[minind] =  minnode.next
        return minnode

    if not lists:
        return None

    root = get_min_node(lists)
    if not root:
        return None

    node = root
    while node:
        prev = node
        node = get_min_node(lists)
        prev.next = node
    return root