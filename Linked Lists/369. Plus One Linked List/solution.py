# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        current = head

        result = ''

        while current:
            result+=self.int_to_str(current.val)
            current = current.next
        
        n = self.int_to_str(self.str_to_int(result) + 1)

        tail = ListNode()
        dummy = tail

        for c in n:
            tail.next = ListNode(self.str_to_int(c))
            tail = tail.next
        
        return dummy.next
    
    def int_to_str(self, n):
        
        result = ''

        while n >0:
            digit = n % 10
            result = chr(digit+ord('0')) + result
            n//=10
        return result if len(result) != 0 else '0'
    
    def str_to_int(self, s):

        result = 0

        for c in s:

            digit = ord(c) - ord('0')
            result = result* 10 + digit

        return result
        


if __name__ == '__main__':

    """ Example 1: """

    head = ListNode()

    print(Solution().plusOne(head))