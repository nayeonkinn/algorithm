# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def inorder(n):
            nonlocal idx
            if n > len(nums):
                return
            
            root = TreeNode()
            root.left = inorder(2 * n)
            root.val = nums[idx]
            idx += 1
            root.right = inorder(2 * n + 1)
            return root
        
        idx = 0
        return inorder(1)