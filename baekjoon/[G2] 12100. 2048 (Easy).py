import sys

sys.stdin = open('input/12100.txt')  # 16
input = sys.stdin.readline

def merge(nums):
    k = 0
    while k < len(nums) - 1:
        if nums[k] == nums[k + 1]:
            nums[k] *= 2
            nums[k + 1] = 0
            k += 2
        else:
            k += 1
    
    return list(filter(None, nums))

def move(arr, d):
    new_arr = [[0] * n for _ in range(n)]

    if d == 0:  # up
        for i in range(n):
            nums = [arr[j][i] for j in range(n) if arr[j][i]]

            for idx, val in enumerate(merge(nums)):
                new_arr[idx][i] = val
        
    elif d == 1:  # down
        for i in range(n):
            nums = [arr[j][i] for j in range(n - 1, -1, -1) if arr[j][i]]

            for idx, val in enumerate(merge(nums), 1):
                new_arr[n - idx][i] = val

    elif d == 2:  # left
        for i in range(n):
            nums = list(filter(None, arr[i]))

            for idx, val in enumerate(merge(nums)):
                new_arr[i][idx] = val

    else:  # right
        for i in range(n):
            nums = list(filter(None, arr[i]))[::-1]

            for idx, val in enumerate(merge(nums), 1):
                new_arr[i][n - idx] = val
    
    return new_arr

def backtracking(arr, cnt):
    global answer

    if cnt == 5:
        answer = max(answer, max(map(max, arr)))
        return
    
    for i in range(4):
        backtracking(move(arr, i), cnt + 1)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0

backtracking(arr, 0)

print(answer)