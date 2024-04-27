import sys

sys.stdin = open('input/19941-1.txt')  # 8, 7

n, k = map(int, input().split())
info = list(input())

answer = 0

for i in range(n):
    if info[i] == 'P':
        for j in range(-k, k + 1):
            if 0 <= i + j < n and info[i + j] == 'H':
                answer += 1
                info[i + j] = None
                break

print(answer)