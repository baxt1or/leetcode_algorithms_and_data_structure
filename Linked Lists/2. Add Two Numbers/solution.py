from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        som = int(self.convert(l1)[::-1]) + int(self.convert(l2)[::-1])

        dummy = ListNode()
        tail = dummy

        for n in str(som)[::-1]:
            tail.next = ListNode(int(n))
            tail = tail.next
        return dummy.next
    

    def convert(self, head):
        current = head
        ans = ''

        while current:
            ans+=str(current.val)
            current = current.next
        return ans
        