import sys

sys.stdin = open('input/22866.txt')  # 1 2  0  3 2  2 2  4 4  3 4  4 6  0

n = int(input())
arr = list(map(int, input().split()))

cnt = [0] * n
num = [1e9] * n

for rng in [range(n), range(n)[::-1]]:
    stack = []

    for i in rng:
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        if stack:
            cnt[i] += len(stack)

            if abs(stack[-1] - i) < abs(num[i] - i):
                num[i] = stack[-1]

        stack.append(i)

for c, n in zip(cnt, num):
    print(c, n + 1 if c else '')