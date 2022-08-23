import sys
sys.stdin = open('input/1223.txt')

for tc in range(1, 11):
    N = int(input())
    string = input()

    result = ''
    stack = []
    for s in string:
        if s == '+':
            while stack:
                result += stack.pop()
            stack.append(s)
        elif s == '*':
            while stack and stack[-1] == '*':
                result += stack.pop()
            stack.append(s)
        else:
            result += s
    while stack:
        result += stack.pop()
    
    stack = []
    for r in result:
        if r == '+':
            x = int(stack.pop())
            y = int(stack.pop())
            stack.append(y + x)
        elif r == '*':
            x = int(stack.pop())
            y = int(stack.pop())
            stack.append(y * x)
        else:
            stack.append(r)

    print(f'#{tc} {stack[-1]}')