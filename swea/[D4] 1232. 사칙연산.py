import sys
sys.stdin = open('input/1232.txt')

def cal(num):
    if len(node[num]) == 4:
        a, b, c = node[num][1], int(node[num][2]), int(node[num][3])
        if a == '+':
            return cal(b) + cal(c)
        elif a == '-':
            return cal(b) - cal(c)
        elif a == '*':
            return cal(b) * cal(c)
        else:
            return cal(b) / cal(c)
    else:
        return int(node[num][1])

for t in range(1, 11):
    N = int(input())
    node = [[]] + [input().split() for _ in range(N)]
    print(f'#{t} {int(cal(1))}')
