import sys

sys.stdin = open('input/1620.txt')  # Pikachu  26  Venusaur  16  14
input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}

for i in range(1, N + 1):
    name = input().strip()
    dic[name] = str(i)
    dic[str(i)] = name

answer = []

for _ in range(M):
    print(dic[input().strip()])