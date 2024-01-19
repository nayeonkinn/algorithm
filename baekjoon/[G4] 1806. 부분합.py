import sys

sys.stdin = open('input/1806.txt')  # 2
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

answer = 1e9

i = 0
j = 0
cnt = 1
summ = nums[0]

while 0 <= i <= j and 0 <= j < n:
    if summ < s:
        j += 1
        if j == n:
            break
        cnt += 1
        summ += nums[j]
    else:
        answer = min(answer, cnt)

        summ -= nums[i]
        i += 1
        cnt -= 1

print(answer if answer != 1e9 else 0)