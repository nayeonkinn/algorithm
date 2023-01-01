import sys
sys.stdin = open('input/6603.txt')

def dfs(idx, num):
    if len(num) == 6:
        print(*num)
        return
    
    for i in range(idx, k):
        dfs(i + 1, num + [S[i]])

while True:
    k, *S = map(int, input().split())
    if k == 0:
        break
    dfs(0, [])
    print()
