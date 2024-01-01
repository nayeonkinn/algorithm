import sys
sys.stdin = open('input/1629.txt')  # 4

def power(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return power(a, b // 2, c) ** 2 % c
    else:
        return power(a, b // 2, c) ** 2 * a % c

a, b, c = map(int, input().split())
print(power(a, b, c))