import sys

sys.stdin = open('input/27172-1.txt')  # 1 1 -2, 0 0 0 0
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

answer = {i: 0 for i in nums}
max_num = max(nums)

for num in nums:
    for i in range(num * 2, max_num + 1, num):
        if answer.get(i, None) is not None:
            answer[num] += 1
            answer[i] -= 1

print(*answer.values())