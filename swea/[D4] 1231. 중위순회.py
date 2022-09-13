import sys
sys.stdin = open('input/1231.txt')

def inorder(n):
    if n <= V:
        if len(info[n]) > 2:
            inorder(int(info[n][2]))
        print(info[n][1], end = '')
        if len(info[n]) > 3:
            inorder(int(info[n][3]))

for i in range(1, 11):
    print(f'#{i}', end = ' ')
    V = int(input())
    info = [[]] + [input().split() for _ in range(V)]
    inorder(1)
    print()