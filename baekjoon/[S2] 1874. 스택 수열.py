import sys

sys.stdin = open('input/1874-1.txt')  # +  +  +  +  -  -  +  +  -  +  +  -  -  -  -  -, NO
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

stack, answer = [], []
now = 1

for num in nums:
    while now <= num:
        stack.append(now)
        now += 1
        answer.append('+')
    if stack.pop() != num:
        answer = ['NO']
        break
    answer.append('-')

print('\n'.join(answer))