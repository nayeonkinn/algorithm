class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = '0'
            for d in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                di = i + d[0]
                dj = j + d[1]
                if 0 <= di < m and 0 <= dj < n and grid[di][dj] == '1':
                    dfs(di, dj)
        
        m, n, cnt = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1

        return cnt