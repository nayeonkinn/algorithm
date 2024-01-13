import sys

sys.stdin = open('input/1003-1.txt')  # 1 0  0 1  1 2, 5 8  10946 17711

# 1
t = int(input())
for _ in range(t):
    n = int(input())

    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        dp_0 = [0] * (n + 1)
        dp_1 = [0] * (n + 1)

        dp_0[:2] = [1, 0]
        dp_1[:2] = [0, 1]

        for i in range(2, n + 1):
            dp_0[i] = dp_0[i - 1] + dp_0[i - 2]
            dp_1[i] = dp_1[i - 1] + dp_1[i - 2]

        print(dp_0[-1], dp_1[-1])

# 2
dp = [[0] * 2 for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1

for i in range(2, 41):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(*dp[n])