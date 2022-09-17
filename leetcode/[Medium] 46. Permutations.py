class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(i, p):
            if i == len(nums):
                permutation.append(p)
                return
            
            for j in nums:
                if j not in p:
                    backtracking(i + 1, p + [j])
            
        permutation = []
        backtracking(0, [])
        return permutation