import sys

sys.stdin = open('input/1027-1.txt')  # 7, 0, 2, 4, 6

n = int(input())
arr = list(map(int, input().split()))

answer = [0] * n

for i in range(n - 1):
    slope = -1e9

    for j in range(i + 1, n):
        if slope < (arr[i] - arr[j]) / (i - j):
            slope = (arr[i] - arr[j]) / (i - j)
            answer[i] += 1
            answer[j] += 1

print(max(answer))