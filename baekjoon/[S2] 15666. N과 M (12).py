import sys

sys.stdin = open('input/15666-1.txt')  # 2  4, 1 1  1 7  1 9  7 7  7 9  9 9, 1 1 1 1  1 1 1 2  1 1 2 2  1 2 2 2  2 2 2 2
input = sys.stdin.readline

def dfs(num, depth):
    if depth == M:
        print(*answer)
        return
    
    for i in range(nums.index(num), len(nums)):
        answer.append(nums[i])
        dfs(nums[i], depth + 1)
        answer.pop()

N, M = map(int, input().split())
nums = sorted(set(map(int, input().split())))

answer = []

dfs(nums[0], 0)