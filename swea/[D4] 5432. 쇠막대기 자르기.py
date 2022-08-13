import sys
sys.stdin = open('input/5432.txt', 'r')

def isStick(sticks, i):
    if i + 1 < len(sticks) and sticks[i] == '(' and sticks[i + 1] == ')':
        return True
    return False

T = int(input())
for t in range(T):
    sticks = input()
    stick = piece = i = 0
    while i < len(sticks):
        if isStick(sticks, i):
            piece += stick
            i += 2
            continue
        if sticks[i] == '(':
            stick += 1
        elif sticks[i] == ')':
            stick -= 1
            piece += 1
        i += 1
    print(f'#{t + 1} {piece}')