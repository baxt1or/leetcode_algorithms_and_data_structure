# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        res = []

        while current:
            res.append(current.val)
            current = current.next
        
        nums = sorted(res)

        dummy = ListNode()
        tail = dummy

        for n in nums:
            tail.next = ListNode(n)
            tail = tail.next
        return dummy.next