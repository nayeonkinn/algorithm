import sys
sys.stdin = open('input/17779-1.txt') # 18, 20 , 23
input = sys.stdin.readline

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
print(city)

1 <= x <= N - 2
2 <= y <= N - 1