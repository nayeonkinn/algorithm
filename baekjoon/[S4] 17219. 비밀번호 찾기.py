import sys

sys.stdin = open('input/17219.txt')  # THEKINGOD  UAENA  IU  siteEAMER
input = sys.stdin.readline

n, m = map(int, input().split())

memo = {}

for _ in range(n):
    site, pw = input().split()
    memo[site] = pw

for _ in range(m):
    site = input().strip()
    print(memo[site])