for case in range(10):
    n = int(input())
    box = list(map(int, input().split()))
    for i in range(n) : 
        box.sort()
        box[0] += 1
        box[-1] -= 1
    print(f'#{case + 1} {max(box) - min(box)}')