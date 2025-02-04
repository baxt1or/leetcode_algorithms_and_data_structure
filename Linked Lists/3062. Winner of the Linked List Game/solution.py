from collections import Counter
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        res = []
        current = head

        while current and current.next is not None:
            if current.val < current.next.val:
                res.append("Odd")
            else:    
                res.append("Even")
            current = current.next
        
        result = [res[i] for i in range(len(res)) if i % 2 == 0]

        count = Counter(result)

        max_freq = max(count.values())

        if list(count.values()).count(max_freq) > 1:
            return "Tie"
        return max(count, key=count.get)
        