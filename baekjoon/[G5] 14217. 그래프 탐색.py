import sys
from collections import defaultdict, deque
sys.stdin = open('input/14217.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
road = defaultdict(list)
for _ in range(m):
    i, j = map(int, input().split())
    road[i].append(j)
    road[j].append(i)

q = int(input())
for _ in range(q):
    a, i, j = map(int, input().split())
    if a == 1:
       road[i].append(j)
       road[j].append(i)
    else:
        road[i].remove(j)
        road[j].remove(i)

    dist = defaultdict(int)
    queue = deque([(1, 1)])
    while queue:
        t, v = queue.popleft()
        if v not in dist:
            dist[v] = t
            for w in road[v]:
                if w not in dist:
                    queue.append((t + 1, w))
    
    for k in range(1, n + 1):
        print(dist[k] - 1, end = ' ')
    print()
