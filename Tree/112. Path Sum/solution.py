from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False
        
        stack = [(root, [root.val])]


        while stack:
            node, cur_val = stack.pop()

            if not node.left and not node.right:
                if sum(cur_val) == targetSum:
                    return True
            
            if node.left:
                stack.append((node.left, cur_val + [node.left.val]))
            if node.right:
                stack.append((node.right, cur_val + [node.right.val]))
        
        return False


a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(8)
a.left = b 
a.right = c 

d = TreeNode(11)
b.left = d 

e = TreeNode(7)
f = TreeNode(2)
d.left = e 
d.right = f 


g  = TreeNode(13)
h = TreeNode(4)
i = TreeNode(1)

c.left = g 
c.right = h 
h.right = i

targetSum = 22


print(Solution().hasPathSum(a, targetSum))