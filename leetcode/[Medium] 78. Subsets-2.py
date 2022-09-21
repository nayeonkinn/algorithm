class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx, subset):
            res.append(subset)
            for i in range(idx, len(nums)):
                dfs(i + 1, subset + [nums[i]])
        
        res = []
        dfs(0, [])
        return res