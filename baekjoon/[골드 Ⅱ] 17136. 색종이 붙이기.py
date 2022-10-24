import sys
sys.stdin = open('input/17136-8.txt') # 0, 4, 5, -1, 7, 4, 6, 5

def backtracking(i, j, cnt):
    global ans
    if ans <= cnt:
        return
    if j == 10:
        backtracking(i + 1, j - 10, cnt)
        return
    if i == 10:
        ans = min(cnt, ans)
        return

    if arr[i][j] == 1:
        for n in range(5):
            ni, nj = i + n, j + n
            if ni < 10 and nj < 10 and arr[ni][nj] and paper[n]:
                for m in range(n + 1):
                    if arr[i + m][j:j + n + 1] != [1] * (n + 1):
                        break
                else:
                    for m in range(n + 1):
                        arr[i + m][j:j + n + 1] = [0] * (n + 1)
                    paper[n] -= 1
                    backtracking(i, j + 1, cnt + 1)
                    paper[n] += 1
                    for m in range(n + 1):
                        arr[i + m][j:j + n + 1] = [1] * (n + 1)
    else:
        backtracking(i, j + 1, cnt)

arr = [list(map(int, input().split())) for _ in range(10)]
ans = 26
paper = [5, 5, 5, 5, 5]

backtracking(0, 0, 0)

if ans != 26:
    print(ans)
else:
    print(-1)