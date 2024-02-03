import sys

sys.stdin = open('input/10773-1.txt')  # 0, 7
input = sys.stdin.readline

k = int(input())

stack = []

for _ in range(k):
    if num := int(input()):
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))