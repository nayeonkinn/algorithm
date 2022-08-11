# import sys
# sys.stdin = open('input1.txt', 'r') # A B B A D
# # sys.stdin = open('input2.txt', 'r') # D B A A

def win(ac, bc) :
    card = [4, 3, 2, 1]
    for c in card :
        A = ac.count(c)
        B = bc.count(c)
        if A > B :
            return 'A'
        elif A < B :
            return 'B'
        elif A == B and c == 1 :
            return 'D'
        else :
            continue

N = int(input())
for n in range(N) :
    a, *ac = list(map(int, input().split()))
    b, *bc = list(map(int, input().split()))
    print(win(ac, bc))