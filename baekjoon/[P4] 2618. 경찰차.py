import sys

sys.stdin = open('input/2618.txt')  # 9  2  2  1
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def calc(car1, car2):
    car3 = max(car1, car2) + 1

    car1_dist = abs(case1[car1][0] - case1[car3][0]) + abs(case1[car1][1] - case1[car3][1])
    car2_dist = abs(case2[car2][0] - case2[car3][0]) + abs(case2[car2][1] - case2[car3][1])
    
    result1 = car1_dist + dist(car3, car2)
    result2 = car2_dist + dist(car1, car3)

    return car3, result1, result2

def dist(car1, car2):
    if dp[car1][car2] != -1:
        return dp[car1][car2]
    
    if car1 == w or car2 == w:
        return 0

    _, result1, result2 = calc(car1, car2)

    dp[car1][car2] = min(result1, result2)

    return dp[car1][car2]

def path(car1, car2):
    if car1 == w or car2 == w:
        return
    
    car3, result1, result2 = calc(car1, car2)

    if result1 < result2:
        print(1)
        path(car3, car2)
    else:
        print(2)
        path(car1, car3)

n = int(input())
w = int(input())

cases = [tuple(map(int, input().split())) for _ in range(w)]
case1 = [[1, 1]] + cases
case2 = [[n, n]] + cases

dp = [[-1] * (w + 1) for _ in range(w + 1)]

print(dist(0, 0))
path(0, 0)