import sys
sys.stdin = open('input.txt', 'r')

def canSkip(map, i, energy, length) :
    for e in range(1, energy + 1) :
        if i + e >= length - 1 or map[i + e] == 1 :
            return True

T = int(input())
for t in range(T) :
    K, N, M = input().split()
    map = [0] * int(N)
    charger = [int(c) for c in input().split()]
    for c in charger :
        map[c - 1] = 1

    energy = int(K)
    cnt = 0
    for i in range(int(N)) :
        energy -= 1
        if energy < 0 :
            cnt = 0
            break
        if map[i] == 1 :
            if canSkip(map, i, energy, int(N)) :
                pass
            else :
                energy = int(K)
                cnt += 1
    print(f'#{t + 1} {cnt}')