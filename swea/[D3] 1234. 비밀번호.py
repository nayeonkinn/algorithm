import sys
sys.stdin = open('input/1234.txt')

for tc in range(1, 11):
    N, password = input().split()
    stack = []
    for char in password:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    print(f'#{tc} {"".join(stack)}')