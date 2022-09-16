import sys
sys.stdin = open('input/1238.txt')

for t in range(1, 11):
    N, V = map(int, input().split())
    temp = list(map(int, input().split()))
    node = [[] for _ in range(101)]
    for i in range(N // 2):
        node[temp[2 * i]].append(temp[2 * i + 1])

    queue = [V]
    visited = [0] * 101
    visited[V] = 1
    while queue:
        V = queue.pop(0)
        for W in node[V]:
            if visited[W] == 0:
                queue.append(W)
                visited[W] = visited[V] + 1

    last = []
    for j in range(101):
        if visited[j] == max(visited):
            last.append(j)

    print(f'#{t} {last[-1]}')