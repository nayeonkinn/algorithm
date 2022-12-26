import sys
sys.stdin = open('input/2805-1.txt') # 15, 36

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2
    take = sum(map(lambda x: x - mid if x > mid else 0, trees))
    if take >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
