import sys

sys.stdin = open('input/9012-1.txt')  # NO  NO  YES  NO  YES  NO, NO  NO  NO
input = sys.stdin.readline

def is_vps(ps):
    stack = []

    for char in ps:
        if char == '(':
            stack.append(char)
        elif stack:
            stack.pop()
        else:
            return 'NO'
    
    return 'NO' if stack else 'YES'

for _ in range(int(input())):
    print(is_vps(input().strip()))