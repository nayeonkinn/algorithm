from collections import Counter
import sys

sys.stdin = open('input/2108-1.txt')  # 2  2  1  10, 4000  4000  4000  0, -2  -2  -1  2, 0  0  0  1
input = sys.stdin.readline

N = int(input())
nums = sorted(int(input()) for _ in range(N))
cnt = sorted(Counter(nums).items(), key=lambda x: (-x[1], x[0]))

print(round(sum(nums) / N))
print(nums[N // 2])
print(cnt[0][0] if N == 1 or cnt[0][1] != cnt[1][1] else cnt[1][0])
print(nums[-1] - nums[0])