
from collections import Counter
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:

        result = [key for key, val in Counter(self.get_elements(head)).items() if val == 1]

        dummy = ListNode()
        tail = dummy

        for n in result:
            tail.next = ListNode(n)
            tail = tail.next
        return dummy.next

    def get_elements(self, head):
        current = head
        res = []

        while current:
            res.append(current.val)
            current = current.next
        return res
        