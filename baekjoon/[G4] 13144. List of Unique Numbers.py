import sys

sys.stdin = open('input/13144-1.txt')  # 15, 12, 5

n = int(input())
nums = list(map(int, input().split()))

visited = [False] * 100001
answer = 0
end = 0

for start in range(n):
    while end < n:
        if visited[nums[end]]:
            visited[nums[start]] = False
            break
        else:
            visited[nums[end]] = True
            end += 1
            answer += end - start

print(answer)