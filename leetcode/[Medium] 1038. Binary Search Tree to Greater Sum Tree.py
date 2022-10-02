# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    value = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        root.right = self.bstToGst(root.right)
        self.value += root.val
        root.val = self.value
        root.left = self.bstToGst(root.left)

        return root