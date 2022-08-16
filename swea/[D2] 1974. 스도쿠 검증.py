import sys
sys.stdin = open('input/1974.txt', 'r')

def check(sudoku):
    num = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    sudoku_T = [[sudoku[j][i] for j in range(9)] for i in range(9)]
    sudoku_S = [[] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            sudoku_S[3 * (i // 3) + j // 3].append(sudoku[i][j])

    for i in range(9):
        if set(sudoku[i]) != num:
            return 0
        if set(sudoku_T[i]) != num:
            return 0
        if set(sudoku_S[i]) != num:
            return 0
    return 1

T = int(input())
for t in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{t + 1} {check(sudoku)}')