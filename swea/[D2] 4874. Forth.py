import sys
sys.stdin = open('input/4874.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    code = input().split()
    stack = []
    for c in code:
        if c == '.':
            if len(stack) == 1:
                result = stack[-1]
            else:
                result = 'error'
                break

        elif c in '+-*/':
            if len(stack) >= 2:
                x, y = stack.pop(), stack.pop()
            else:
                result = 'error'
                break

            if c == '+':
                stack.append(int(y) + int(x))
            elif c == '-':
                stack.append(int(y) - int(x))
            elif c == '*':
                stack.append(int(y) * int(x))
            elif c == '/':
                stack.append(int(y) // int(x))

        else:
            stack.append(c)

    print(f'#{tc} {result}')