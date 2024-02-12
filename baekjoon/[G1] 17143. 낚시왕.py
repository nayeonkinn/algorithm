import sys

sys.stdin = open('input/17143-1.txt')  # 22, 0, 22, 4
input = sys.stdin.readline

R, C, M = map(int, input().split())

if not M:
    print(0)
    exit()

sharks = {}
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r - 1, c - 1)] = (s, d, z)

direction = ((), (-1, 0), (1, 0), (0, 1), (0, -1))
answer = 0

for x in range(C):
    catch = 1e9
    for (r, c), (s, d, z) in sharks.items():
        if c == x:
            catch = min(catch, r)
    if catch != 1e9:
        answer += sharks[(catch, x)][2]
        del sharks[(catch, x)]

    sharks2 = {}
    for (r, c), (s, d, z) in sharks.items():
        r = (r + direction[d][0] * s) % ((R - 1) * 2)
        c = (c + direction[d][1] * s) % ((C - 1) * 2)
        if r >= R:
            r = 2 * (R - 1) - r
            d = 1 if d == 2 else 2
        elif c >= C:
            c = 2 * (C - 1) - c
            d = 3 if d == 4 else 4

        temp = sharks2.get((r, c))
        if temp and temp[2] < z or not temp:
            sharks2[(r, c)] = (s, d, z)

    sharks = sharks2

print(answer)