import copy

N = int(input())

dices = []
for i in range(N) :
    dices.append(list(map(int, input().split())))

def opposite(dice, val) :
    ref = [5, 3, 4, 1, 2, 0]
    for i in range(6) :
        if dice[i] == val :
            return dice[ref[i]]

maxx = 0
for num in dices[0] :
    total = 0
    newdices = copy.deepcopy(dices)
    up = opposite(dices[0], num)
    for dice in newdices :
        down = up
        up = opposite(dice, down)
        dice.remove(down)
        dice.remove(up)
        total += max(dice)
    if total > maxx :
        maxx = total

print(maxx)