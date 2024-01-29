import sys

sys.stdin = open('input/1654.txt')  # 200
input = sys.stdin.readline

def binary_search(low, high):
    global answer

    if low > high:
        return

    mid = (low + high) // 2

    cnt = 0
    for cable in cables:
        cnt += cable // mid
    
    if cnt >= n:
        answer = mid
        binary_search(mid + 1, high)
    else:
        binary_search(low, mid - 1)

k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]

answer = 0

binary_search(1, max(cables))
# low 값을 0으로 시작한다면 high가 1일 때 mid가 0이 되면서 16번째 줄에서 ZeroDivisionError 발생
# 문제 조건에서 모든 값이 자연수이므로 0이 아닌 1으로 설정하여 해결

print(answer)