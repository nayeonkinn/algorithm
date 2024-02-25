import sys

sys.stdin = open('input/2630.txt')  # 9  7
input = sys.stdin.readline

def divide(i, j, n):
    color = arr[i][j]
    
    for x in range(i, i + n):
         for y in range(j, j + n):
              if arr[x][y] != color:
                   divide(i, j, n // 2)
                   divide(i + n // 2, j, n // 2)
                   divide(i, j + n // 2, n // 2)
                   divide(i + n // 2, j + n // 2, n // 2)
                   return

    answer[color] += 1              

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = [0, 0]

divide(0, 0, n)

for a in answer:
     print(a)