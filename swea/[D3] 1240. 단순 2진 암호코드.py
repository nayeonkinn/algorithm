import sys
sys.stdin = open('input/1240.txt')

rule = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    for i in range(N):
        if sum(arr[i]) > 1:
            code = arr[i]
            break
    for j in range(M - 1, -1, -1):
        if code[j] == 1:
            code = code[j - 55:j + 1]
            break
    code = ''.join(list(map(str, code)))
    validation = total = 0
    for k in range(0, 56, 7):
        v = 1 if k // 7 % 2 else 3
        validation += v * rule[''.join(code[k:k + 7])]
        total += rule[''.join(code[k:k + 7])]
    if validation % 10:
        total = 0
    print(f'#{t} {total}')