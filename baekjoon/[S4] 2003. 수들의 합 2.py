import sys

sys.stdin = open('input/2003-1.txt')  # 3, 3

N, M = map(int, input().split())
arr = list(map(int, input().split()))

total = arr[0]
left, right = 0, 0
answer = 0

while left < N:
    if total == M:
        answer += 1

    if total >= M:
        total -= arr[left]
        left += 1
    else:
        if right == N - 1:
            break
        right += 1
        total += arr[right]

print(answer)