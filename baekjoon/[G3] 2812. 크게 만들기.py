import sys
sys.stdin = open('input/2812-1.txt')  # 94, 3234, 775841

n, k = map(int, input().split())
numbers = input()
stack = []

for number in numbers:
    while stack and number > stack[-1] and k > 0:
        stack.pop()
        k -= 1
    stack.append(number)

if k:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))
