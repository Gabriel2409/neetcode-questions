# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if not list1:
        return list2
    if not list2:
        return list1

    head1 = list1
    head2 = list2

    before_first = ListNode(val=-1)
    head = before_first

    while head1 or head2:
        if not head1:
            head.next = head2
            head2 = head2.next
        elif not head2:
            head.next = head1
            head1 = head1.next
        elif head1.val <= head2.val:
            head.next = head1
            head1 = head1.next
        else:
            head.next = head2
            head2 = head2.next
        head = head.next

    return before_first.next


if __name__ == "__main__":

    n1 = [ListNode(val=1), ListNode(val=2), ListNode(val=4)]
    n1[0].next = n1[1]
    n1[1].next = n1[2]
    n2 = [ListNode(val=1), ListNode(val=3), ListNode(val=4)]
    n2[0].next = n2[1]
    n2[1].next = n2[2]
    merge_two_lists(n1[0], n2[0])
