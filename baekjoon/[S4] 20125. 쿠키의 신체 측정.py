import sys

sys.stdin = open('input/20125-1.txt')  # 3 3  1 1 1 1 1, 3 6  3 2 3 4 1, 2 5  4 4 3 4 4
input = sys.stdin.readline

n = int(input())

answer = [0] * 5

for i in range(n):
    temp = input().strip()
    if '*' in temp:
        hi, hj = i + 1, temp.index('*')
        break

temp = input().strip()
answer[0] = temp[:hj].count('*')
answer[1] = temp[hj + 1:].count('*')

for i in range(n - hi - 1):
    temp = input().strip()
    if temp[hj] == '*':
        answer[2] += 1
    if temp[hj - 1] == '*':
        answer[3] += 1
    if temp[hj + 1] == '*':
        answer[4] += 1

print(hi + 1, hj + 1)
print(*answer)