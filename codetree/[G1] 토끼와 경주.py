import sys, heapq

sys.stdin = open('input/토끼와 경주-2.txt')  # 151, 122
input = sys.stdin.readline


def init(data):
    global N, M, P
    N, M, P, *temp = data

    for i in range(P):
        pid, d = temp[2 * i], temp[2 * i + 1]
        heapq.heappush(rabbits, [0, 2, 1, 1, pid])
        dist[pid] = d
        score[pid] = 0


def move(i, j, d):
    position = []

    # right
    right = (j + d) % (2 * (M - 1)) or 2 * (M - 1) or 2 * (M - 1)
    if right > M:
        right = 2 * M - right
    heapq.heappush(position, [-(i + right), -i, -right])

    # down
    down = (i + d) % (2 * (N - 1)) or 2 * (N - 1)
    if down > N:
        down = 2 * N - down
    heapq.heappush(position, [-(down + j), -down, -j])

    # left
    left = (M - j + 1 + d) % (2 * (M - 1)) or 2 * (M - 1)
    if left <= M:
        left = M + 1 - left
    else:
        left = left - M + 1
    heapq.heappush(position, [-(i + left), -i, -left])

    # up
    up = (N - i + 1 + d) % (2 * (N - 1)) or 2 * (N - 1)
    if up <= N:
        up = N + 1 - up
    else:
        up = up - N + 1
    heapq.heappush(position, [-(up + j), -up, -j])

    di, dj = heapq.heappop(position)[1:]
    return -di, -dj


def race(data):
    global left_score
    K, S = data
    now_rabbits = []

    for _ in range(K):
        jump, _, i, j, pid = heapq.heappop(rabbits)
        di, dj = move(i, j, dist[pid])
        score[pid] -= di + dj
        left_score += di + dj
        heapq.heappush(rabbits, [jump + 1, di + dj, di, dj, pid])
        heapq.heappush(now_rabbits, [-(di + dj), -di, -dj, -pid])

    _, _, _, pid = heapq.heappop(now_rabbits)
    score[-pid] += S


def change(data):
    pid, L = data
    dist[pid] *= L


def best():
    print(max(score.values()) + left_score)


Q = int(input())
N, M, P, left_score = 0, 0, 0, 0
rabbits, dist, score= [], {}, {}

for _ in range(Q):
    command, *data = map(int, input().split())

    if command == 100:
        init(data)
    elif command == 200:
        race(data)
    elif command == 300:
        change(data)
    elif command == 400:
        best()
