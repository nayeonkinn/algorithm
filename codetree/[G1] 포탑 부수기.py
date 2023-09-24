import sys
from collections import deque

sys.stdin = open('input/포탑 부수기-3.txt')  # 17, 17, 4269
input = sys.stdin.readline


def is_turret_one():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                cnt += 1
            if cnt > 1:
                return False
    return True


def find_attacker(turn):
    candidate = []
    minimum = 5000
    for i in range(n):
        for j in range(m):
            if arr[i][j] <= 0:
                continue
            elif arr[i][j] < minimum:
                minimum = arr[i][j]
                candidate = [(i, j)]
            elif arr[i][j] == minimum:
                candidate.append((i, j))

    if len(candidate) > 1:
        t = turn - 1
        while t >= 0:
            if set(history[t]) & set(candidate):
                candidate = [*set(history[t]) & set(candidate)]
                break
            t -= 1

    if len(candidate) > 1:
        candidate = [(i, j) for i, j in candidate if i + j == sum(max(candidate, key = lambda x: x[0] + x[1]))]

    if len(candidate) > 1:
        candidate = [max(candidate, key = lambda x: x[1])]

    for t in range(turn):
        if candidate[0] in history[t]:
            history[t].remove(candidate[0])
            break
    history[turn] = [candidate[0]]

    return candidate[0]


def find_target(turn, attacker):
    candidate = []
    maximum = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] <= 0:
                continue
            elif arr[i] == attacker[0] and arr[j] == attacker[1]:
                continue
            elif arr[i][j] > maximum:
                maximum = arr[i][j]
                candidate = [(i, j)]
            elif arr[i][j] == maximum:
                candidate.append((i, j))

    if len(candidate) > 1:
        t = 0
        while t < turn:
            if set(history[t]) & set(candidate):
                candidate = [*set(history[t]) & set(candidate)]
                break
            t += 1

    if len(candidate) > 1:
        candidate = [(i, j) for i, j in candidate if i + j == sum(min(candidate, key = lambda x: x[0] + x[1]))]

    if len(candidate) > 1:
        candidate = [min(candidate, key = lambda x: x[1])]
    
    return candidate[0]


def rasor(attacker, target):
    queue = deque([[*attacker, []]])
    visited = [[False] * m for _ in range(n)]
    # print(queue)
    flag = False

    while queue:
        i, j, route = queue.popleft()
        if (i, j) == target:
            flag = True
            break
        
        for di, dj in delta_4:
            ni, nj = (di + i) % n, (dj + j) % m
            if arr[ni][nj] > 0 and not visited[ni][nj]:
                queue.append([ni, nj, route + [(ni, nj)]])
                visited[ni][nj] = True
    
    if not flag:
        return False
    
    for i in range(n):
        for j in range(m):
            if (i, j) in route:
                attack = arr[attacker[0]][attacker[1]]
                if (i, j) == target:
                    arr[i][j] -= attack
                else:
                    arr[i][j] -= attack // 2
            elif arr[i][j] <= 0 or (i, j) == attacker:
                pass
            else:
                arr[i][j] += 1
    
    return True


def shell(attacker, target):
    attack = arr[attacker[0]][attacker[1]]
    route = [(target[0], target[1])]
    
    for di, dj in delta_8:
        ni, nj = (di + target[0]) % n, (dj + target[1]) % m
        if arr[ni][nj] > 0 and (ni, nj) != (attacker[0], attacker[1]):
            route.append((ni, nj))
            arr[ni][nj] -= attack // 2
    
    arr[target[0]][target[1]] -= attack

    for i in range(n):
        for j in range(m):
            if (i, j) not in route and arr[i][j] > 0 and (i, j) != attacker:
                arr[i][j] += 1


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
history = {0: [(i, j) for i in range(n) for j in range(m)]}
delta_4 = ((0, 1), (1, 0), (0, -1), (-1, 0))
delta_8 = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

for turn in range(1, k + 1):
    if is_turret_one():
        break

    attacker = find_attacker(turn)
    target = find_target(turn, attacker)
    
    arr[attacker[0]][attacker[1]] += n + m

    if not rasor(attacker, target):
        shell(attacker, target)

print(max(*sum(arr, [])))
