import sys
from turtle import circle
sys.stdin = open("input.txt", "r")

x, y = map(int, input().split())
cnt = int(input())
store = [list(map(int, input().split())) for i in range(cnt)]
d = list(map(int, input().split()))

total = 0
for s in store :
    direction = (d[0], s[0])
    criteria = d[1] + s[1]
    if d[0] == s[0] :
        total += abs(d[1] - s[1])  
    elif set(direction) == {1, 2} :
        total += min(criteria, 2 * x - criteria) + y
    elif set(direction) == {3, 4} :
        total += min(criteria, 2 * y - criteria) + x
    elif set(direction) == {1, 3} :
        total += criteria
    elif set(direction) == {2, 4} :
        total += x + y - criteria
    elif direction == (1, 4) :
        total += x - d[1] + s[1]
    elif direction == (4, 1) :
        total += d[1] + x - s[1]
    elif direction == (3, 2) :
        total += y - d[1] + s[1]
    elif direction == (2, 3) :
        total += d[1] + y - s[1]

print(total)