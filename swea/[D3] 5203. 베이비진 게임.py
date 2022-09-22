import sys
sys.stdin = open('input/5203.txt')

def is_baby_gin(p):
    for i in range(10):
        if p[i] > 2:
            return True
        if i < 8 and p[i] > 0 and p[i + 1] > 0 and p[i + 2] > 0:
            return True

T = int(input())
for t in range(1, T + 1):
    temp = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    answer = 0

    for i in range(6):
        p1[temp[2 * i]] += 1
        p2[temp[2 * i + 1]] += 1
        if i > 2:
            if is_baby_gin(p1):
                answer = 1
                break
            if is_baby_gin(p2):
                answer =  2
                break

    print(f'#{t} {answer}')
