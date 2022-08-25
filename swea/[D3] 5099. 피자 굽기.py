import sys
sys.stdin = open('input/5099.txt', 'r')

def my_enumerate(C):
    i = 1
    cheese = []
    for c in C:
        cheese.append([i, c])
        i += 1
    return cheese

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    
    q = []
    cheese = my_enumerate(C)
    for _ in range(N):
        q.append(cheese.pop(0))

    while len(q) != 1:
        q[0][1] //= 2
        if q[0][1] == 0:
            q.pop(0)
            if cheese:
                q.append(cheese.pop(0))
        else:
            q.append(q.pop(0))
    
    print(f'#{tc} {q[0][0]}')