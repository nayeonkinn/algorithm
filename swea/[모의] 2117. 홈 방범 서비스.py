import sys
sys.stdin = open('input/2117.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(N):
            house = set()
            for k in range(1, N + 2):
                for x in range(k):
                    y = k - 1 - x
                    for d in ((x, y), (x, -y), (-x, y), (-x, -y)):
                        di = i + d[0]
                        dj = j + d[1]
                        if 0 <= di < N and 0 <= dj < N and city[di][dj] == 1:
                            house.add((di, dj))
                cost = k * k + (k - 1) * (k - 1)
                if len(house) > answer and len(house) * M - cost >= 0:
                    answer = len(house)

    print(f'#{t} {answer}')
