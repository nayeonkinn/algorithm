class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        queue = [(m // 2, n // 2)]
        visited = [[False] * n for _ in range(m)]
        visited[m // 2][n // 2] = True
        
        while queue:
            i, j = queue.pop(0)

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                for di, dj in ((i - 1, j), (i, j - 1)):
                    if 0 <= di < m and 0 <= dj < n and not visited[di][dj]:
                        queue.append((di, dj))
                        visited[di][dj] = True
            else:
                for di, dj in ((i + 1, j), (i, j + 1)):
                    if 0 <= di < m and 0 <= dj < n and not visited[di][dj]:
                        queue.append((di, dj))
                        visited[di][dj] = True

        return False