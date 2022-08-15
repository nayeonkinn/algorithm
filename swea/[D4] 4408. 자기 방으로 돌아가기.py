import sys
sys.stdin = open('input/4408.txt')

def roomNum(n):
    if int(n) % 2:
        return int(n) // 2
    else:
        return int(n) // 2 - 1

T = int(input())
for t in range(T):
    N = int(input())
    room = [list(map(roomNum, input().split())) for _ in range(N)]
    hall = [0] * 200
    for r in room:
        r.sort()
        for i in range(r[0], r[1] + 1):
            hall[i] += 1
    print(f'#{t + 1} {max(hall)}')