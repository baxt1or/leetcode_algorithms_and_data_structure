from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        stack = [(root, [root.val])]
        res = []

        while stack:
            node, cur_val = stack.pop()

            if not node.left and not node.right:
                if sum(cur_val) == targetSum:
                    res.append(cur_val)
             
            if node.left:
                stack.append((node.left, cur_val+[node.left.val]))
            
            if node.right:
                stack.append((node.right, cur_val + [node.right.val]))
        
        return res


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
j = TreeNode(5)

c.left = g 
c.right = h 
h.right = i
h.left = j

targetSum = 22

print(Solution().pathSum(a, targetSum))