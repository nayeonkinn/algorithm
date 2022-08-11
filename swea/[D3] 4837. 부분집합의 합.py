# import sys
# sys.stdin = open('input.txt', 'r')

def sum(arr) :
    total = 0
    for i in arr :
        total += i
    return total

A = list(range(1, 13))

T = int(input())
for t in range(T) :
    result = 0
    N, K = map(int, input().split())
    
    for i in range(1 << 12) :
        arr = []
        for j in range(12) :
            if i & (1 << j) :
                arr.append(A[j])
        if sum(arr) == K and len(arr) == N:
            result += 1
    print(f'#{t + 1} {result}')