import sys
sys.stdin = open('input/17471-1.txt') # 1, 0, -1, 9

from collections import deque

def check(lst):
    queue = deque([lst[0]])
    visited = [0] * (N + 1)
    visited[lst[0]] = 1
    cnt = 1
    while queue:
        v = queue.popleft()
        for w in node[v]:
            if w in lst and visited[w] == 0:
                visited[w] = 1
                cnt += 1
                queue.append(w)

    if cnt == len(lst):
        return True
    else:
        return False

def compare(A):
    a = 0
    for i in A:
        a += population[i - 1]
    b = sum(population) - a
    return abs(a - b)

N = int(input())
population = list(map(int, input().split()))
temp = [list(map(int, input().split())) for _ in range(N)]
node = [[] for _ in range(N + 1)]
for i in range(N):
    cnt, *args = temp[i]
    for j in range(cnt):
        node[i + 1].append(args[j])

diff = 1000
for i in range(1 << N):
    A, B, cnt = [], [], 0
    for j in range(N):
        if i & (1 << j):
            cnt += 1
            A.append(j + 1)
        else:
            B.append(j + 1)
    if 0 < cnt < N:
        if check(A) and check(B):
            diff = min(compare(A), diff)

if diff == 1000:
    print(-1)
else:
    print(diff)
