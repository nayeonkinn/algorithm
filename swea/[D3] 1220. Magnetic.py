import sys
sys.stdin = open('1220.txt', 'r')

for tc in range(1, 11):
    input()
    table = [list(map(int, input().split())) for _ in range(100)]
    
    cnt = 0
    for j in range(100):
        i = 99
        while i > -1:
            if table[i][j] == 2:
                for k in range(i)[::-1]:
                    if table[k][j] == 1:
                        cnt += 1
                        i = k
                        break
            i -= 1

    print(f'#{tc} {cnt}')