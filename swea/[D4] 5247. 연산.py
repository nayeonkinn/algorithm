import sys
sys.stdin = open('input/5247.txt')

def bfs():
    queue = [(N, 0)]
    visited = [0] * 1000001
    visited[N] = 1

    while queue:
        v, cnt = queue.pop(0)
        if v == M:
            return cnt
        
        for w in [v + 1, v - 1, v * 2, v - 10]:
            if 0 < w <= min(M + 10, 1000000) and visited[w] == 0:
                queue.append((w, cnt + 1))
                visited[w] = 1

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs()}')
