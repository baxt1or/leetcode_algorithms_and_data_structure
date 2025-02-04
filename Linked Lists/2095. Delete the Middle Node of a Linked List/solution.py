from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = self.get_middle_node(head)
        temp = head
        prev = None 

        if head is not None and head.next is None:
            return None

        if not head and not head.next:
            return None

        while temp and temp != mid:
            prev = temp
            temp = temp.next 
        
        if prev:
            prev.next = temp.next

        return head
        


    
    def get_middle_node(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        return slow


if __name__ == "__main__":
    ls = ListNode()

    sol = Solution()

    sol.deleteMiddle(ls)