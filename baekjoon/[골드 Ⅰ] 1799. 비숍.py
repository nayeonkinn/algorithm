import sys
sys.stdin = open('input/1799.txt')


def is_promising(x, y, type):
    if not (0 <= x < n and 0 <= y < n):
        return True
    if bishop[x][y]:
        return False

    if type == 0:
        return is_promising(x - 1, y - 1, 1) and is_promising(x - 1, y + 1, 2)
    elif type == 1:
        return is_promising(x - 1, y - 1, 1)
    elif type == 2:
        return is_promising(x - 1, y + 1, 2)


def backtracking(idx, cnt, type):
    if idx == len(candidate[type]):
        answer[type] = max(cnt, answer[type])
        return

    i, j = candidate[type][idx]
    if is_promising(i, j, 0):
        bishop[i][j] = True
        backtracking(idx + 1, cnt + 1, type)
        bishop[i][j] = False
    backtracking(idx + 1, cnt, type)


n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
odd, even = [], []
for i in range(n):
    for j in range(n):
        if chess[i][j]:
            if (i + j) % 2:
                odd.append((i, j))
            else:
                even.append((i, j))

candidate, answer = [odd, even], [0, 0]
bishop = [[False] * n for _ in range(n)]
backtracking(0, 0, 0)
backtracking(0, 0, 1)
print(sum(answer))
