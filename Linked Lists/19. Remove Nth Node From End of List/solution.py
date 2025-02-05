from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        res = []

        while current:
            res.append(current.val)
            current = current.next
        
        nums = res[::-1]

        del nums[n-1]

        nums = nums[::-1]

        dummy = ListNode()
        tail = dummy

        for n in nums:
            tail.next = ListNode(n)
            tail = tail.next
        return dummy.next
    

if __name__ == "__main__":
    ls = ListNode()
    sol = Solution()
    print(sol.removeNthFromEnd(ls, 2))