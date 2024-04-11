import sys

sys.stdin = open('input/1943.txt')  # 0  1  1
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    coins = sorted([list(map(int, input().split())) for _ in range(N)], reverse=True)  # 큰 동전부터 탐색하기 위해 내림차순 정렬

    total = sum(map(lambda x: x[0] * x[1], coins))
    
    if total % 2:
        print(0)
        continue

    total //= 2
    dp = [1] + [0] * total  # dp[i]: 가진 동전으로 i원을 만들 수 있는지 여부

    for c, n in coins:
        for i in range(total, c - 1, -1):
            if dp[i]:  # 이전 반복문에서 이미 탐색됨
                continue
            if dp[i - c]:
                for j in range(i, min(i + c * n, total) + 1, c):
                    dp[j] = 1
        if dp[-1]:
            break

    print(dp[-1])