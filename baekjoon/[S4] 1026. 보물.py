import sys
sys.stdin = open('input/1026-1.txt') # 18, 80, 528

N = int(input())
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()))

print(sum([A[i] * B[i] for i in range(N)]))