import sys

sys.stdin = open('input/15961-1.txt')  # 5, 4
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]

check = [0] * (d + 1)
cnt = 0
answer = 0

for i in range(k):
    if not check[arr[i]]:
        cnt += 1
    check[arr[i]] += 1

for l in range(1, N):
    r = (l + k - 1) % N

    check[arr[l - 1]] -= 1
    if not check[arr[l - 1]]:
        cnt -= 1

    if not check[arr[r]]:
        cnt += 1
    check[arr[r]] += 1

    if check[c]:
        answer = max(answer, cnt)
    else:
        answer = max(answer, cnt + 1)

print(answer)