import sys
sys.stdin = open('input/1244.txt')

def dfs(idx, cnt):
    global max_price
    if cnt == n:
        max_price = max(int(''.join(nums)), max_price)
        return

    for i in range(idx, k):
        for j in range(i + 1, k):
            if nums[i] <= nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i, cnt + 1)
                nums[i], nums[j] = nums[j], nums[i]

    if not max_price:
        if (n - cnt) % 2:
            nums[-1], nums[-2] = nums[-2], nums[-1]
        dfs(idx, n)

T = int(input())
for t in range(1, T + 1):
    nums, n = input().split()
    nums, n = list(nums), int(n)
    k = len(nums)
    max_price = 0
    dfs(0, 0)
    print(f'#{t} {max_price}')
