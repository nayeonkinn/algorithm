import sys
sys.stdin = open('input/1966.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    print(f'#{t + 1} {" ".join(map(str, num))}')