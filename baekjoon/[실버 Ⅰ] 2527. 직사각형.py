import sys
sys.stdin = open("input.txt", "r")

for i in range(4) :
    a, b, c, d, e, f, g, h = list(map(int, input().split()))
    
    if c < e or g < a :
        x = 0
    elif c == e or g == a :
        x = 1
    else :
        x = 2

    if d < f or h < b :
        y = 0
    elif d == f or h == b :
        y = 1
    else :
        y = 2

    if x == 0 or y == 0 :
        print('d')
    elif x == 1 and y == 1 :
        print('c')
    elif x == 1 or y == 1 :
        print('b')
    else :
        print('a')