import sys
sys.stdin = open('input/1224.txt', 'r')

for tc in range(1, 11):
    input()
    string = input()

    result = ''
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif s == '*':
            while stack and stack[-1] == '*':
                result += stack.pop()
            stack.append(s)
        elif s == '+':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            result += s
    while stack:
        result += stack.pop()

    stack = []
    for r in result:
        if r in '*+':
            x = int(stack.pop())
            y = int(stack.pop())
            if r == '*':
                stack.append(x * y)
            else:
                stack.append(x + y)
        else:
            stack.append(r)

    print(f'#{tc} {stack[-1]}')