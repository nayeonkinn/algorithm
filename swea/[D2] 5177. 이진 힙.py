import sys
sys.stdin = open('input/5177.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    heap, last = [0] * (N + 1), 0

    for num in nums:
        last += 1
        heap[last] = num

        p, c = last // 2, last
        while heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p, c = p // 2, p

    idx, total = N // 2, 0
    while idx:
        total += heap[idx]
        idx //= 2
    
    print(f'#{t} {total}')
