n = int(input())
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n)]
mod = 1000000000

# dp[x][y][z]: x번째 자리에서 숫자 y일 경우의 비트값 z에 해당하는 경우의 수

for y in range(1, 10):
    dp[0][y][1 << y] = 1

for x in range(1, n):
    for y in range(10):
        for z in range(1 << 10):
            if y > 0:
                dp[x][y][z | (1 << y)] += dp[x - 1][y - 1][z]
            if y < 9:
                dp[x][y][z | (1 << y)] += dp[x - 1][y + 1][z]
            
            dp[x][y][z | (1 << y)] %= mod

print(sum(dp[n - 1][y][-1] for y in range(10)) % mod)