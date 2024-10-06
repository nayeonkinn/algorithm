import sys

sys.stdin = open('input/1037-1.txt')  # 8, 4, 24, 185192

n = int(input())
factors = sorted(map(int, input().split()))

print(factors[0] ** 2 if len(factors) == 1 else factors[0] * factors[-1])