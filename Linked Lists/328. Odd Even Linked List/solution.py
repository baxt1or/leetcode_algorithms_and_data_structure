from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds = []
        evens = []
        current = head
        i = 0

        while current:
            if i % 2 ==0:
                evens.append(current.val)
            else:
                odds.append(current.val)
            current = current.next
            i+=1
        
        r = evens + odds

        dummy = ListNode()
        tail = dummy

        for n in r:
            tail.next = ListNode(n)
            tail = tail.next
        return dummy.next
        