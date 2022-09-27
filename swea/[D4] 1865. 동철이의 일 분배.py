import sys
sys.stdin = open('input/1865.txt')

def backtracking(idx, p):
    global answer
    if p <= answer:
        return
    if idx == N:
        answer = max(p, answer)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            backtracking(idx + 1, p * P[idx][i] * 0.01)
            visited[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    answer, visited = 0, [0] * N
    backtracking(0, 1)
    print(f'#{tc} {answer * 100:.6f}')
