import sys
sys.stdin = open('input/1859.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    price = list(map(int, input().split()))[::-1]
    maxprice = price[0]
    profit = 0
    for i in range(1, N):
        if price[i] < maxprice:
            profit += maxprice - price[i]
        else:
            maxprice = price[i]
    print(f'#{t + 1} {profit}')