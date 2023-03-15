
from typing import  Optional

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

def reorder_list( head: Optional[ListNode]) -> None:
    """
    Works but is too slow
    """

    node = head
    cur = node 
    while True:
        if not node.next or not node.next.next :
            h = head
            while h:
                print(h)
                h = h.next

            return head

        while cur.next:
            prev = cur
            cur = cur.next
        
        cur.next = node.next
        prev.next = None
        node.next = cur
        node = cur.next





n1 = [ListNode(val=1), ListNode(val=2), ListNode(val=3), ListNode(val=4), ListNode(val=5)]
n1[0].next = n1[1]
n1[1].next = n1[2]
n1[2].next = n1[3]
n1[3].next = n1[4]
reorder_list(n1[0])
