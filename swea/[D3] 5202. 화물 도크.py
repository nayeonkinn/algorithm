import sys
sys.stdin = open('input/5202.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    time = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x: x[1])

    answer = 0
    for i in range(N):
        cnt = 0
        end = time[i][0]
        for j in range(i, N):
            s, e = time[j]
            if s >= end:
                cnt += 1
                end = e
            else:
                continue
        answer = max(cnt, answer)

    print(f'#{t} {answer}')
