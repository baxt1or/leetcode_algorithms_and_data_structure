from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        mid = self.get_middle_element(head=current)

        while current and current != mid:
            current = current.next
        
        return current

    def get_middle_element(self, head):
        slow  = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    
    node = ListNode()

    sol = Solution()

    print(sol.middleNode(node))