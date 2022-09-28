# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal longest
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            longest = max(left + right + 2, longest)
            return max(left, right) + 1
        
        longest = 0
        dfs(root)
        return longest