import sys

sys.stdin = open('input/1509-1.txt')  # 22, 1, 8, 5

s = ' ' + input()
t = len(s)

pd = [[False] * t for _ in range(t)]  # pd[i][j]: i ~ j 문자열이 팰린드롬인지 여부
dp = [1e9] * t  # dp[i]: i번째 자리까지 최소 팰린드롬 분할 개수

def palindrome():
    for i in range(t):
        pd[i][i] = True

    for i in range(t - 1):
        if s[i] == s[i + 1]:
            pd[i][i + 1] = True

    for i in range(t - 2, -1, -1):
        for j in range(i + 2, t):
            if s[i] == s[j] and pd[i + 1][j - 1]:  # 맨 앞과 맨 뒤 문자가 같고, 사이 문자열이 팰린드롬이라면
                pd[i][j] = True

def minimum():
    dp[0] = 0
    dp[1] = 1
    for i in range(2, t):
        for j in range(i):
            if pd[j + 1][i]:  # j+1 ~ i 문자열이 팰린드롬이라면
                dp[i] = min(dp[i], dp[j] + 1)  # i까지의 최소 팰린드롬 개수는 j까지의 최소 팰린드롬 개수 + 1

    # for i in range(1, t):  # 이런 로직도 가능
    #     for j in range(i + 1, t):
    #         if pd[i][j]:
    #             dp[j] = min(dp[j], dp[i - 1] + 1)
    #         else:
    #             dp[j] = min(dp[j], dp[j - 1] + 1)

palindrome()
minimum()

print(dp[-1])