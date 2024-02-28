import sys
from bisect import bisect_left

sys.stdin = open('input/2568.txt')  # 3  1  3  4
input = sys.stdin.readline

n = int(input())

arr = sorted(list(map(int, input().split())) for _ in range(n))

bs = [arr[0][1]]
record = [0] * n

for i in range(1, n):
    if arr[i][1] < bs[-1]:
        bs[idx := bisect_left(bs, arr[i][1])] = arr[i][1]
        record[i] = idx
    else:
        bs.append(arr[i][1])
        record[i] = len(bs) - 1

answer = []
idx = len(bs) - 1

for i in range(n - 1, -1, -1):
    if record[i] == idx:
        idx -= 1
    else:
        answer.append(arr[i][0])
        
print(len(answer))
for a in answer[::-1]:
    print(a)