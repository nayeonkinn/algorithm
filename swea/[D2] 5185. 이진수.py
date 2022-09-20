import sys
sys.stdin = open('input/5185.txt')

char = '0123456789ABCDEF'
T = int(input())
for t in range(1, T + 1):
    N, h = input().split()
    b = ''
    for i in range(int(N)):
        for j in range(16):
            if h[i] == char[j]:
                sub_b = ''
                for _ in range(4):
                    sub_b = str(j % 2) + sub_b
                    j //= 2
                b += sub_b
                break

    print(f'#{t} {b}')