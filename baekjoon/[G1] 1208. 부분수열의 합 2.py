import sys
from collections import defaultdict

sys.stdin = open('input/1208.txt')  # 1
input = sys.stdin.readline

def subsum(nums):
    result = [0]
    for n in nums:
        result += [r + n for r in result]
    return result

n, s = map(int, input().split())
nums = list(map(int, input().split()))

dic = defaultdict(int)
answer = 0

for i in subsum(nums[:n//2]):
    dic[i] += 1

for i in subsum(nums[n//2:]):
    answer += dic[s - i]

print(answer if s else answer - 1)