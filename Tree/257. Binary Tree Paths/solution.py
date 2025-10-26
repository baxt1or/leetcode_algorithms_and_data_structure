from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        stack = [(root, [root.val])]
        res = []

        while stack:
            node, cur_val = stack.pop()

            if not node.left and not node.right:
                res.append(cur_val)
            
            if node.left:
                stack.append((node.left, cur_val + [node.left.val]))

            if node.right:
                stack.append((node.right, cur_val + [node.right.val]))

        
        for i in range(len(res)):
            res[i] = "->".join([str(x) for x in res[i]])
        
        
        return res

        
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

a.left = b
a.right = c

d = TreeNode(5)
f = TreeNode(6)

b.left = d 
b.right = f




print(Solution().binaryTreePaths(a))


[
    [[1], 1], 
    [[3], 3], 
    [[2], 2], 
    [[6], 6], 
    [[5], 5]
]