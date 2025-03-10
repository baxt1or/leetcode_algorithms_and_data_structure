from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []

        current = head

        while current:
            res.append(current.val)
            current = current.next
        return res == res[::-1]


if __name__ == "__main__":
    ls = ListNode()

    sol = Solution()
    
    print(sol.isPalindrome(ls))