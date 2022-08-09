import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T) :
    N = int(input())
    cards = [int(n) for n in input()]

    dic = {}
    for card in cards :
        if dic.get(card) == None :
            dic[card] = 0
        dic[card] += 1

    maxV = 0
    for key in dic :
        if dic[key] > maxV or (dic[key] == maxV and key > maxK) :
            maxV = dic[key]
            maxK = key
    print(f'#{t + 1} {maxK} {maxV}')