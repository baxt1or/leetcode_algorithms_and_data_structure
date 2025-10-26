from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            current = stack.pop()

            res.append(current.val)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        
        return res
    

a = TreeNode(1)
b = TreeNode(2)
e = TreeNode(3)
c = e
d = TreeNode(5)


a.left = b 
a.right = c

b.right = d
b.left = TreeNode(4)
d.left = TreeNode(6)
d.right = TreeNode(7)

f = TreeNode(8)

e.right = f 
f.left = TreeNode(9)

sol = Solution()

assert sol.preorderTraversal(a) == [1,2,4,5,6,7,3,8,9], "Ouput check"