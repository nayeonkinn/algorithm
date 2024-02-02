import sys
from bisect import bisect_left

sys.stdin = open('input/14003.txt')  # 4  10 20 30 50

n = int(input())
arr = list(map(int, input().split()))

bs = [arr[0]]  # bs에 담기는 수열은 LIS와 길이는 일치하나 숫자는 다를 수 있음
record = [0] * n  # 각 원소가 bs에 저장되는 인덱스를 저장하여 LIS 역추적

for i in range(1, n):
    if arr[i] <= bs[-1]:
        bs[idx := bisect_left(bs, arr[i])] = arr[i]
        record[i] = idx
    else:
        bs.append(arr[i])
        record[i] = len(bs) - 1

answer = []
idx = len(bs) - 1
for i in range(n - 1, -1, -1):
    if record[i] == idx:
        answer.append(arr[i])
        idx -= 1

print(len(bs))
print(*answer[::-1])