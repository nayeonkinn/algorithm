import sys
sys.stdin = open('input/1215.txt', 'r')

def is_palindrome(arr):
    return arr == arr[::-1]

for tc in range(1, 11):
    l = int(input())
    cnt = 0
    board = [list(input()) for _ in range(8)]
    board_T = [[board[j][i] for j in range(8)] for i in range(8)]
    for i in range(8):
        for j in range(9 - l):
            if is_palindrome(board[i][j:j + l]):
                cnt += 1
            if is_palindrome(board_T[i][j:j + l]):
                cnt += 1
    print(f'#{tc} {cnt}')