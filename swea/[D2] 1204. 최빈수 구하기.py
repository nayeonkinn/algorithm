T = int(input())

for t in range(1, T + 1):
    input()
    numbers = list(map(int, input().split()))
    d = {}
    for num in numbers :
        if d.get(num) == None :
            d[num] = 0
        d[num] += 1
    print(f'#{t} {sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0]}')