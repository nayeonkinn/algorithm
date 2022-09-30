import sys
sys.stdin = open('input/2115.txt')

def get_honey(hive):
    answer = 0
    for i in range(1 << M):
        c = 0
        honey = 0
        for j in range(M):
            if i & (1 << j):
                c += hive[j]
                honey += hive[j] ** 2
        if c <= C:
            answer = max(honey, answer)

    return answer

T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    hive = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(N - M + 1):
            honey1 = get_honey(hive[i][j:j + M])
            for k in range(j + M, N - M + 1):
                honey2 = get_honey(hive[i][k:k + M])
                answer = max(honey1 + honey2, answer)
            for l in range(i + 1, N):
                for m in range(N - M + 1):
                    honey2 = get_honey(hive[l][m:m + M])
                    answer = max(honey1 + honey2, answer)

    print(f'#{tc} {answer}')
