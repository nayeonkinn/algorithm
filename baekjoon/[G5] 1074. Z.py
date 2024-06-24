import sys

sys.stdin = open('input/1074-1.txt')  # 11, 63, 0, 63, 262143, 786432

N, r, c = map(int, input().split())

answer = 0

while N:
    N -= 1

    if r < 2 ** N and c >= 2 ** N:  # 2
        answer += (2 ** N) ** 2
        c -= 2 ** N

    elif r >= 2 ** N and c < 2 ** N:  # 3
        answer += (2 ** N) ** 2 * 2
        r -= 2 ** N

    elif r >= 2 ** N and c >= 2 ** N:  # 4
        answer += (2 ** N) ** 2 * 3
        r -= 2 ** N
        c -= 2 ** N

print(answer)