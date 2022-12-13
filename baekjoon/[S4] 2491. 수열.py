N = int(input())
S = list(map(int, input().split()))

maxx = 1

up = 1
for i in range(1, N) :
    if S[i] >= S[i - 1] :
        up += 1
    else :
        up = 1
    if up > maxx :
        maxx = up  

down = 1
for i in range(1, N) :
    if S[i] <= S[i - 1] :
        down += 1
    else :
        down = 1
    if down > maxx :
        maxx = down

print(maxx)