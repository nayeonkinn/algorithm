import sys

sys.stdin = open('input/2239.txt')  # 143628579
                                    # 572139468
                                    # 986754231
                                    # 391542786
                                    # 468917352
                                    # 725863914
                                    # 237481695
                                    # 619275843
                                    # 854396127
input = sys.stdin.readline

def check(i, j):
    nums = [True] * 10

    for x in range(9):
        nums[sudoku[i][x]] = False
        nums[sudoku[x][j]] = False
    for x in range((i // 3) * 3, (i // 3) * 3 + 3):
        for y in range((j // 3) * 3, (j // 3) * 3 + 3):
            nums[sudoku[x][y]] = False

    return [i for i, v in enumerate(nums) if i and v]

def backtracking(i, j):
    if i == 9:
        for i in range(9):
            print("".join(list(map(str, sudoku[i]))))
        exit()
    
    if sudoku[i][j]:
        backtracking(i + (j + 1) // 9, (j + 1) % 9)
        return

    for num in check(i, j):
        sudoku[i][j] = num
        backtracking(i + (j + 1) // 9, (j + 1) % 9)
        sudoku[i][j] = 0

sudoku = [list(map(int, input().strip())) for _ in range(9)]

backtracking(0, 0)