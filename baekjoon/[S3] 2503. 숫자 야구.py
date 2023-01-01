import sys
from itertools import permutations as p
sys.stdin = open('input/2503.txt')
input = sys.stdin.readline

nums = list(p('123456789', 3))
n = int(input())
for _ in range(n):
    est, strike, ball = map(lambda x: str(x) if len(x) > 1 else int(x), input().split())
    temp = []
    for num in nums:
        s = sum([1 if est[j] == num[j] else 0 for j in range(3)])
        b = len(set(est) & set(num)) - s
        if s == strike and b == ball:
            temp.append(num)
    nums = temp
print(len(nums))