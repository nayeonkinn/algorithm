import sys

sys.stdin = open('input/7568.txt')  # 2 2 1 2 5
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = [1] * n

for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            answer[j] += 1
        elif arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            answer[i] += 1

print(*answer)