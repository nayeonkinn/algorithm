import sys

sys.stdin = open('input/18110-1.txt')  # 6, 13
input = sys.stdin.readline

# round 내장함수는 엄밀히 따지면 반올림 함수가 아니라 가장 가까운 10의 ndigits 배수 값을 제공하는 함수
# 이때, 양 쪽이 똑같이 가깝다면 (ex. 0.5이라면) 짝수를 선택하여 반올림
# ex. round(0.5) = 1, round(1.5) = 3, round(2.5) = 2

def round(num):
    if num - num // 1 < 0.5:
        return int(num // 1)
    else:
        return int(num // 1) + 1

n = int(input())

if not n:
    print(0)
    exit()

arr = sorted([int(input()) for _ in range(n)])

offset = round(n * 0.15)
if offset:
    arr = arr[offset:-offset]

print(round(sum(arr) / (n - offset * 2)))