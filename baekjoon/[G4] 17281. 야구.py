import sys
sys.stdin = open('input/17281-1.txt') # 1, 4, 43, 46, 216, 89


from itertools import permutations

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
max_score = 0

for order in list(map(list, permutations(range(1, 9)))):
    order.insert(3, 0)
    score, inning, player, out = 0, 0, 0, 0
    first, second, third = False, False, False

    while inning < n:
        result = info[inning][order[player]]
        if result == 0:
            out += 1
        elif result == 1:
            score += third
            first, second, third = True, first, second
        elif result == 2:
            score += second + third
            first, second, third = False, True, first
        elif result == 3:
            score += first + second + third
            first, second, third = False, False, True
        else:
            score += 1 + first + second + third
            first, second, third = False, False, False
        
        player = (player + 1) % 9
        if out >= 3:
            inning += 1
            first, second, third, out = False, False, False, 0

    max_score = max(score, max_score)

print(max_score)
