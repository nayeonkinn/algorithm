import sys
sys.stdin = open('input/4869.txt', 'r')

def combi(a, b):
    result = 1
    for i in range(a, a - b, -1):
        result *= i
    for j in range(b, 0, -1):
        result //= j
    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    a = N // 10
    b = 0
    result = 0
    while a >= b:
        result += combi(a, b) * (2 ** b)
        a -= 1
        b += 1

    print(f'#{tc} {result}')