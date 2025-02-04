from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import sys
sys.set_int_max_str_digits(100000)

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        res = []
        while current:
            res.append(str(current.val))
            current = current.next
        
        
        num = int("".join(res)) *2 
        r = [x for x in str(num)]

        dummy = ListNode()
        tail = dummy

        for x in r:
            tail.next = ListNode(int(x))
            tail = tail.next
        return dummy.next
