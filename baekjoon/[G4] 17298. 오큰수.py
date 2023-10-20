import sys
sys.stdin = open('input/17298-1.txt')  # 5 7 7 -1, -1 8 8 -1
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [-1] * n

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)
