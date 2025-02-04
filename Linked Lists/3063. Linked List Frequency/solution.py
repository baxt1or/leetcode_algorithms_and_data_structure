from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = {}

        current = head

        while current:
            count[current.val] = count.get(current.val, 0)+1
            current = current.next
        
        dummy = ListNode()
        tail = dummy

        for freq in count.values():
            tail.next = ListNode(freq)
            tail  = tail.next
            
        return dummy.next