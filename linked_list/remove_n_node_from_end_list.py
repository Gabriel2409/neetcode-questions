from typing import Optional
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next:
            next_val = self.next.val
        else:
            next_val = None
        return f"{self.val}->{next_val}"

def remove_n_node(head: Optional[ListNode], n: int) -> Optional[ListNode]:

    l = head

    r = head

    i = 0
    while i < n:
        r = r.next
        i = i + 1

    if r is None:
        return head.next

    while True:
        r = r.next
        if not r:
            l.next = l.next.next
            return head
        l = l.next

n1 = [ListNode(val=1), ListNode(val=2), ListNode(val=3), ListNode(val=4), ListNode(val=5)]
n1[0].next = n1[1]
n1[1].next = n1[2]
n1[2].next = n1[3]
n1[3].next = n1[4]
final = remove_n_node(n1[0], 2)
while final:
    print(final)
    final = final.next