import sys
sys.stdin = open('input/1952.txt')

def dfs(idx, price):
    global min_price
    if price > min_price:
        return
    while idx < 12 and plan[idx] == 0:
        idx += 1
    if idx >= 12:
        min_price = min(price, min_price)
        return
    
    dfs(idx + 1, price + d * plan[idx])
    dfs(idx + 1, price + m)
    dfs(idx + 3, price + q)
    dfs(idx + 12, price + y)

T = int(input())
for t in range(1, T + 1):
    d, m, q, y = map(int, input().split())
    plan = list(map(int, input().split()))
    min_price = 3000 * 12 * 31
    dfs(0, 0)
    print(f'#{t} {min_price}')