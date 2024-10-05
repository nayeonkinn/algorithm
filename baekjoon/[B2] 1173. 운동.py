import sys

sys.stdin = open('input/1173-1.txt')  # 10, 109, -1, 30050, 40

N, m, M, T, R = map(int, input().split())

answer, time, pulse = 0, 0, m

while time != N:
    if m + T > M:
        answer = -1
        break

    if pulse + T <= M:
        time += 1
        pulse += T
    else:
        pulse = max(m, pulse - R)

    answer += 1

print(answer)