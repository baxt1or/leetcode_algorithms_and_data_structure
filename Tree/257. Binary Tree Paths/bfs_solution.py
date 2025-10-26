from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        if not root:
            return []
        
        queue = [(root, [root.val])]
        res = []

        while queue:
            node, val = queue.pop(0)

            if not node.left and node.right:
                res.append(val)
            
            if node.right:
                queue.append((node.right, val + [node.right.val]))
            
            if node.left:
                queue.append((node.left, val+[node.left.val]))
        
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

c.left = g 
c.right = h 
h.right = i

print(Solution().binaryTreePaths(a))