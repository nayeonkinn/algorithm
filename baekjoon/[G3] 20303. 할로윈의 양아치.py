import sys

sys.stdin = open('input/20303-3.txt')  # 57, 0
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])

    return parent[a]

n, m, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

friend = [0] * (n + 1)
candy = [0] * (n + 1)

for i in range(1, n + 1):
    root = find(i)  # union-find 시 경로 압축을 했더라도 입력 순서에 따라 반영되지 않을 수 있음 -> find 함수를 통해 루트를 찾아야 함 (한참 고생하다..)
    friend[root] += 1
    candy[root] += arr[i]

dp = [0] * k  # dp[i]: i명의 아이가 울 때 얻을 수 있는 최대 사탕의 수

for i in range(1, n + 1):
    if not friend[i]:
        continue
    for j in range(k - 1, friend[i] - 1, -1):  # 역순으로 계산함으로써 참고하지 않아야 할 값을 참고하는 경우 방지 (j - friend[i])
        dp[j] = max(dp[j], dp[j - friend[i]] + candy[i])

print(dp[-1])