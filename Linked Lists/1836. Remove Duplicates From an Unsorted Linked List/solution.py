from collections import Counter
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:

        count = {}
        current = head

        while current:
            count[current.val] = count.get(current.val, 0) + 1 
            current = current.next
        
        dummy = ListNode()
        tail = dummy

        for key,val in count.items():
            if val == 1:
                tail.next = ListNode(key)
                tail = tail.next
        return dummy.next
        