import sys
sys.stdin = open('input/18917.txt')  # 8 6 9 7 4 2

M = int(sys.stdin.readline())
total = 0
xor = 0

for _ in range(M):
    query, *num = map(int, sys.stdin.readline().split())

    if query == 1:
        total += num[0]
        xor ^= num[0]

    elif query == 2:
        total -= num[0]
        xor ^= num[0]

    elif query == 3:
        sys.stdout.write(str(total) + '\n')

    else:
        sys.stdout.write(str(xor) + '\n')
