import sys
from collections import deque

sys.stdin = open('input/포탑 부수기-3.txt')  # 17, 17, 4269
input = sys.stdin.readline


def is_turret_one():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                cnt += 1
            if cnt > 1:
                return False
    return True


def find_attack(t):
    attack = None
    minimum = 5000

    for i in range(n):
        for j in range(m):
            if board[i][j] <= 0:
                continue
            
            if board[i][j] < minimum:
                minimum = board[i][j]
                attack = (i, j)
            elif board[i][j] == minimum:
                if history[attack[0]][attack[1]] < history[i][j]:
                    attack = (i, j)
                elif history[attack[0]][attack[1]] == history[i][j]:
                    if attack[0] + attack[1] < i + j:
                        attack = (i, j)
                    elif attack[0] + attack[1] == i + j:
                        if attack[1] < j:
                            attack = (i, j)

    history[attack[0]][attack[1]] = t

    return attack


def find_target(attack):
    target = None
    maximum = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] <= 0:
                continue
            elif board[i] == attack[0] and board[j] == attack[1]:
                continue
            
            if board[i][j] > maximum:
                maximum = board[i][j]
                target = (i, j)
            elif board[i][j] == maximum:
                if history[target[0]][target[1]] > history[i][j]:
                    target = (i, j)
                elif history[target[0]][target[1]] == history[i][j]:
                    if target[0] + target[1] > i + j:
                        target = (i, j)
                    elif target[0] + target[1] == i + j:
                        if target[1] > j:
                            target = (i, j)

    return target


def attack_and_repair(attack, target, related):
    power = board[attack[0]][attack[1]]

    for i in range(n):
        for j in range(m):
            if board[i][j] <= 0 or (i, j) == attack:
                continue

            if (i, j) == target:
                board[i][j] -= power
            elif (i, j) in related:
                board[i][j] -= power // 2
            else:
                board[i][j] += 1


def laser(attack, target):
    queue = deque([[*attack, []]])
    visited = [[False] * m for _ in range(n)]
    success = False

    while queue:
        i, j, route = queue.popleft()
        if (i, j) == target:
            success = True
            break
        
        for di, dj in delta_4:
            ni, nj = (di + i) % n, (dj + j) % m
            if board[ni][nj] > 0 and not visited[ni][nj]:
                queue.append([ni, nj, route + [(ni, nj)]])
                visited[ni][nj] = True
    
    if not success:
        return False
    
    attack_and_repair(attack, target, route)

    return True


def shell(attack, target):
    related = [(target[0], target[1])]
    
    for di, dj in delta_8:
        ni, nj = (di + target[0]) % n, (dj + target[1]) % m
        if board[ni][nj] > 0 and (ni, nj) != (attack[0], attack[1]):
            related.append((ni, nj))
    
    attack_and_repair(attack, target, related)


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
history = [[0] * m for _ in range(n)]
delta_4 = ((0, 1), (1, 0), (0, -1), (-1, 0))
delta_8 = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

for t in range(1, k + 1):
    if is_turret_one():
        break

    attack = find_attack(t)
    target = find_target(attack)
    
    board[attack[0]][attack[1]] += n + m

    if not laser(attack, target):
        shell(attack, target)

print(max(*sum(board, [])))
