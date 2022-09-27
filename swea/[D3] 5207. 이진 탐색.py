import sys
sys.stdin = open('input/5207.txt')

def binary_search(l, r, i):
    global flag, before
    if l <= r:
        m = (l + r) // 2
        if i == A[m]:
            return
        elif i < A[m]:
            if before == 'r' or not before:
                before = 'l'
            elif before == 'l':
                flag = False
                return
            binary_search(l, m - 1, i)
        else:
            if before == 'l' or not before:
                before = 'r'
            elif before == 'r':
                flag = False
                return
            binary_search(m + 1, r, i)
    else:
        flag = False

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    answer = 0
    for i in B:
        flag, before = True, ''
        binary_search(0, N - 1, i)
        if flag:
            answer += 1
    print(f'#{tc} {answer}')
