import sys

sys.stdin = open('input/9252.txt')  # 4  ACAK
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
# 문자열 자체를 dp 배열 안에 계속 더해가는 방식으로 구현하면 시간 초과 -> 숫자로 dp 진행 후 dp 배열 역추적

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(answer := dp[-1][-1])
if answer:
    result = ''

    i, j = len(s1), len(s2)
    while i != 0 and j != 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            result += s1[i - 1]
            i -= 1
            j -= 1
    
    print(result[::-1])