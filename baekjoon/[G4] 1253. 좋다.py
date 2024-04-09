import sys

sys.stdin = open('input/1253.txt')  # 8

def is_good(i, num):
    temp = nums[:i] + nums[i + 1:]
    start, end = 0, n - 2

    while start < end:
        x = temp[start] + temp[end]

        if x > num:
            end -= 1
        elif x < num:
            start += 1
        else:
            return True

n = int(input())
nums = sorted(map(int, input().split()))

answer = 0

for i in range(n):
    if is_good(i, nums[i]):
        answer += 1

print(answer)