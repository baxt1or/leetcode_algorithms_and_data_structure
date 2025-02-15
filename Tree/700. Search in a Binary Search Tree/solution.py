from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return None
        
        if root.val == val:
            return self.preorder(root)

        left_node = self.searchBST(root.left, val)

        if left_node:
            return left_node
        
        return self.searchBST(root.right, val)
    
    def preorder(self, root : TreeNode):

        if not root:
            return None
        
        new_node = TreeNode(root.val)

        new_node.left = self.preorder(root.left)
        new_node.right = self.preorder(root.right)

        return new_node

def print_preorder(root:TreeNode):

    if root:
        print(root.val, end=" ")
        print_preorder(root.left)
        print_preorder(root.right)

if __name__ == '__main__':
    
    """ Example 1: """
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7)

    sol = Solution().searchBST(root, 2)

    print_preorder(sol)