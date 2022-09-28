# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        depth = 0
        
        while q:
            depth += 1
            for _ in range(len(q)):
                sub_root = q.popleft()
                if sub_root.left:
                    q.append(sub_root.left)
                if sub_root.right:
                    q.append(sub_root.right)
        
        return depth