from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.convert(list1)
        l2 = self.convert(list2)

        l = l1 + l2

        l = sorted(l)

        r = self.convert_back(l)

        return r
    
    def convert(self, head):
        current = head
        res = []

        while current:
            res.append(current.val)
            current = current.next
        return res

    def convert_back(self, nums):
        dummy = ListNode()
        tail = dummy

        for n in nums:
            tail.next = ListNode(n)
            tail = tail.next
        return dummy.next
        