from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    visited = [[False] * m for _ in range(n)]
        
    oil_info = {i: 0 for i in range(m)}
    
    for i in range(n):
        for j in range(m):
            if not land[i][j] or visited[i][j]:
                continue

            queue = deque([])
            queue.append((i, j))
            
            visited[i][j] = True
            
            oil = 0
            columns = set()
            
            while queue:
                x, y = queue.popleft()
                
                oil += 1
                columns.add(y)

                for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < m and land[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                
            for column in columns:
                oil_info[column] += oil

    return max(oil_info.values())


# land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]  # 9
land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]  # 16

print(solution(land))