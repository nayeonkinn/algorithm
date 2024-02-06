import sys

sys.stdin = open('input/11050.txt')  # 10

n, k = map(int, input().split())

# 풀이 1
def bino_coef(n, k):
    cache = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        cache[i][0] = 1
    for i in range(k + 1):
        cache[i][i] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            cache[i][j] = cache[i - 1][j] + cache[i - 1][j - 1]
    
    return cache[n][k]

# 풀이 2
def bino_coef(n, k):
    if k > n:
        return 0
    
    cache = [[-1] * (n + 1) for _ in range(n + 1)]

    def choose(cnt, x):  # cnt번의 기회에서 x만큼 선택했을 때, n번의 기회에서 k만큼 선택하는 경우의 수
        if cnt == n:
            return x == k
        
        if cache[cnt][x] != -1:
            return cache[cnt][x]
        
        cache[cnt][x] = choose(cnt + 1, x) + choose(cnt + 1, x + 1)
        return cache[cnt][x]
    
    return choose(0, 0)

print(bino_coef(n, k))