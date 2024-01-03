import sys
sys.stdin = open('input/1918-1.txt')  # ABC+*, AB+, ABC*+, ABC*+DE/-
input = sys.stdin.readline

infix = input()
postfix = ''
stack = []

for c in infix:
    if c.isalpha():
        postfix += c

    else:
        if c == '(':
            stack.append(c)
        elif c in '*/':
            while stack and stack[-1] not in '(+-':
                postfix += stack.pop()
            stack.append(c)
        elif c in '+-':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

while stack:
    postfix += stack.pop()

print(postfix)