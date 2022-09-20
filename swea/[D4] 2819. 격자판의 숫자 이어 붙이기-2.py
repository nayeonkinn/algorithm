import sys
sys.stdin = open('input/2819.txt')

def dfs(idx, i, j, num):
    if idx == 7:
        nums.add(num)
        return
    
    for d in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        di = i + d[0]
        dj = j + d[1]
        if 0 <= di < 4 and 0 <= dj < 4:
            dfs(idx + 1, di, dj, num + arr[di][dj])

T = int(input())
for t in range(1, T + 1):
    arr = [input().split() for _ in range(4)]
    nums = set()
    for i in range(4):
        for j in range(4):
            dfs(1, i, j, arr[i][j])
    print(f'#{t} {len(nums)}')