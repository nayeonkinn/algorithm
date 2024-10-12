import sys

sys.stdin = open('input/17254-1.txt')  # APPLE, LADYBUG
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(map(lambda x: [int(x[1]), int(x[0]), x[2]], [input().split() for _ in range(m)]))

print(''.join(a[2] for a in arr))