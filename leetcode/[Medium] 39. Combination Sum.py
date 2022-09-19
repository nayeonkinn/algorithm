class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(combi, total, idx):
            if total > target:
                return
            if total == target:
                combis.append(combi)
                return
            for i in range(idx, len(candidates)):
                dfs(combi + [candidates[i]], total + candidates[i], i)

        combis = []
        dfs([], 0, 0)
        return combis