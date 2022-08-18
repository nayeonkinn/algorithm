import sys
sys.stdin = open('input/4866.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    s = input()
    result = 1
    stack = []

    for char in s:
        if char == '{' or char == '(':
            stack.append(char)
        elif stack and ((stack[-1] == '{' and char == '}') or (stack[-1] == '(' and char == ')')):
            stack.pop()
        elif char == '}' or char == ')':
            stack.append(char)

    if stack:
        result = 0
    
    print(f'#{tc} {result}')