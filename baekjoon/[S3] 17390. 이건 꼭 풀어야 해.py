import sys

sys.stdin = open('input/17390-1.txt')  # 15  9  3  6  14  9, 5  4  13
input = sys.stdin.readline

N, Q = map(int, input().split())
A = [0] + sorted(map(int, input().split()))

for i in range(1, N + 1):
    A[i] += A[i - 1]

for _ in range(Q):
    L, R = map(int, input().split())
    print(A[R] - A[L - 1])