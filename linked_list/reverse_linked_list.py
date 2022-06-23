# Given the head of a singly linked list, reverse the list, and return the reversed list.
# ex [1,2,3,4] => [4,3,2,1]
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time comp: O(n)
    Space comp : O(1)
    """
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]):
    """
    Time comp: O(n)
    Space comp: O(n)

    More tricky to understand
    [1,2,3]

    head is 1, calls recursion
        head is 2, calls recursion
            head is 3, do nothing return 3. 3 still points to null
        head is 2, new_head is 3. 3 points to 2, 2 points to null. returns 3
    head is 1, new_head is 3. 2 points to 1. 1 points to null. returns 3
    """
    if head is None:
        return None

    new_head = head
    if head.next:
        new_head = reverse_list_recursive(head.next)
        head.next.next = head
        head.next = None

    return new_head
