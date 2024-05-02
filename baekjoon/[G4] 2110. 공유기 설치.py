import sys

sys.stdin = open('input/2110.txt')  # 3
input = sys.stdin.readline

n, c = map(int, input().split())
house = sorted(int(input()) for _ in range(n))

start, end = 1, house[-1] - house[0]

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    last = house[0]
    for h in house[1:]:
        if h - last >= mid:
            cnt += 1
            last = h

    if cnt >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)