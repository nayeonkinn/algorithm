from collections import deque
import sys

sys.stdin = open('input/16234-1.txt')  # 1, 0, 1, 2, 3
input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

candidate = deque(((i, j) for i in range(n) for j in range(i%2, n, 2)))  # 변동 가능성이 있는 나라만 탐색하기 위한 변수 (격자 무늬로 탐색해서 시간 절약)
visited = [[-1] * n for _ in range(n)]  # 배열 한 번만 만들어서 시간 절약
answer = 0

while True:
    for _ in range(len(candidate)):
        i, j = candidate.popleft()

        if visited[i][j] != answer:
            q = deque([(i, j)])
            visited[i][j] = answer
            union = [(i, j)]
            p = arr[i][j]

            while q:
                x, y = q.popleft()

                for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                    if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != answer and l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                        visited[nx][ny] = answer
                        union.append((nx, ny))
                        p += arr[nx][ny]
                        q.append((nx, ny))
            
            if len(union) > 1:
                p //= len(union)
                for x, y in union:
                    arr[x][y] = p
                    candidate.append((x, y))

    if candidate:
        answer += 1
    else:
        break
                    
print(answer)