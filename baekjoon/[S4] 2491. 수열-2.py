import sys
sys.stdin = open('input/2491-1.txt')  # 8, 4, 2
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

up, down = [1] * n, [1] * n

for i in range(n - 1):
    if arr[i] <= arr[i + 1]:
        up[i + 1] = up[i] + 1
    if arr[i] >= arr[i + 1]:
        down[i + 1] = down[i] + 1

print(max(max(up), max(down)))
