import sys

sys.stdin = open('input/9935-1.txt')  # mirkovniz, FRULA

string = input()
bomb = list(input())

stack = []
lb = len(bomb)

for s in string:
    stack.append(s)

    if s == bomb[-1] and stack[-lb:] == bomb:
        del stack[-lb:]

print("".join(stack) if stack else 'FRULA')