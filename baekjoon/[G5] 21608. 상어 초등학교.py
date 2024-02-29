import sys

sys.stdin = open('input/21608-1.txt')  # 54, 1053
input = sys.stdin.readline

n = int(input())

dic = {}
for _ in range(n * n):
    a, *b = map(int, input().split())
    dic[a] = b

arr = [[None] * n for _ in range(n)]
delta = ((1, 0), (-1, 0), (0, 1), (0, -1))

for student, friends in dic.items():
    temp = []

    for i in range(n):
        for j in range(n):
            if not arr[i][j]:
                f_cnt = 0
                e_cnt = 0
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        if arr[ni][nj] in friends:
                            f_cnt += 1
                        if not arr[ni][nj]:
                            e_cnt += 1
                temp.append((-f_cnt, -e_cnt, i, j))
    
    _, _, i, j = sorted(temp)[0]
    arr[i][j] = student

answer = 0
score = [0, 1, 10, 100, 1000]

for i in range(n):
    for j in range(n):
        cnt = 0
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] in dic[arr[i][j]]:
                cnt += 1
    
        answer += score[cnt]
        
print(answer)