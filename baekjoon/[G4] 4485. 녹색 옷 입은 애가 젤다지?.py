import sys, heapq

sys.stdin = open('input/4485.txt')
# Problem 1: 20
# Problem 2: 19
# Problem 3: 36
input = sys.stdin.readline

tc = 1

while n := int(input()):
    cave = [list(map(int, input().split())) for _ in range(n)]

    hq = []
    heapq.heappush(hq, (cave[0][0], 0, 0))

    while hq:
        cost, i, j = heapq.heappop(hq)

        if i == j == n - 1:
            print(f'Problem {tc}: {cost}')
            break

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj

            if 0 <= ni < n and 0 <= nj < n and cave[ni][nj] != -1:
                heapq.heappush(hq, (cost + cave[ni][nj], ni, nj))
                cave[ni][nj] = -1
    
    tc += 1