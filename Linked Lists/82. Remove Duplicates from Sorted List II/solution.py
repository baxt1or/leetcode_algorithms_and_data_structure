from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = {}
        current = head

        while current:
            count[current.val] = count.get(current.val, 0)+1
            current = current.next
        
        result = [key for key, val in count.items() if val == 1]

        dummy = ListNode()
        tail = dummy

        for n in result:
            tail.next = ListNode(n)
            tail = tail.next
        return dummy.next
        