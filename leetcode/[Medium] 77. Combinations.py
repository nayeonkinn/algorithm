class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(i, num, c):
            if i == k:
                combi.append(c)
                return
            
            for j in range(num + 1, n + 1):
                backtracking(i + 1, j, c + [j])
        
        combi = []
        backtracking(0, 0, [])
        return combi