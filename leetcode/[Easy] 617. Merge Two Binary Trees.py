# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(root1, root2):
            if root1 and root2:
                M = TreeNode(root1.val + root2.val)
                M.left = merge(root1.left, root2.left)
                M.right = merge(root1.right, root2.right)
                return M
            elif root1:
                return root1
            elif root2:
                return root2
        
        return merge(root1, root2)