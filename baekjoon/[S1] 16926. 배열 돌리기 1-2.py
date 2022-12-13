import sys
sys.stdin = open('input/16926-1.txt')

from collections import deque

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(min(N, M) // 2):
    q = deque()

    x, y = i, i

    for j in range(i, N - i - 1):
        x = j
        q.append(arr[x][y])

    x += 1

    for j in range(i, M - i - 1):
        y = j
        q.append(arr[x][y])

    y += 1

    for j in range(i, N - i - 1):
        x = N - 1 - j
        q.append(arr[x][y])

    x -= 1

    for j in range(i, M - i - 1):
        y = M - 1 - j
        q.append(arr[x][y])

    q.rotate(R)

    x, y = i, i

    for j in range(i, N - i - 1):
        x = j
        arr[x][y] = q.popleft()

    x += 1

    for j in range(i, M - i - 1):
        y = j
        arr[x][y] = q.popleft()

    y += 1

    for j in range(i, N - i - 1):
        x = N - 1 - j
        arr[x][y] = q.popleft()

    x -= 1

    for j in range(i, M - i - 1):
        y = M - 1 - j
        arr[x][y] = q.popleft()

for i in range(N):
    print(*arr[i])