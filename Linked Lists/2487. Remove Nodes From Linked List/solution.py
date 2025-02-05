from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = self.reverse(head)
        max_val = 0
        res = []
        while current:
            if current.val >= max_val:
                res.append(current.val)
            max_val = max(max_val, current.val)
            current = current.next
        
        nums = res[::-1]
        return self.convert(nums)
        
    
    def reverse(self, head):
        current = head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    def convert(self, nums):
        dummy = ListNode()
        tail = dummy

        for n in nums:
            tail.next = ListNode(n)
            tail = tail.next
        return dummy.next