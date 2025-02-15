from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)



if __name__ == '__main__':

    """ Example 1: """

    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7)))
    root.right = TreeNode(3, right=TreeNode(8, left=TreeNode(9)))

    print(Solution().preorderTraversal(root))