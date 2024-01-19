import sys

sys.stdin = open('input/2467-1.txt')  # -99 98, -2 -1
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

l, r = 0, n -1

min_v = float('inf')
answer = None

while l < r:
    v = arr[l] + arr[r]

    if abs(v) < min_v:
        min_v = abs(v)
        answer = arr[l], arr[r]

    if v == 0:
        break
    elif v > 0:
        r -= 1
    else:
        l += 1

print(*answer)