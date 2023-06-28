import sys
from collections import deque
sys.stdin = open('input/15235.txt')

n = int(input())
pizza = deque(zip(range(n), map(int, input().split())))
answer = [0] * n
cnt = 0

while len(pizza):
    cnt += 1
    idx, left = pizza.popleft()
    answer[idx] = cnt
    left -= 1
    if left:
        pizza.append((idx, left))

print(*answer)
