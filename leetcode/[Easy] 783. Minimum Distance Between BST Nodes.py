# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer, before = 100000, -1
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        
        self.minDiffInBST(root.left)
        if self.before > -1:
            self.answer = min(root.val - self.before, self.answer)
        self.before = root.val
        self.minDiffInBST(root.right)
        
        return self.answer