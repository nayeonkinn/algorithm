# import sys
# sys.stdin = open('input.txt', 'r')

x, y = map(int, input().split())

x_cut = [0, x]
y_cut = [0, y]

n = int(input())
for _ in range(n) :
    temp = input().split()
    if temp[0] == '0' :
        y_cut.append(int(temp[1]))
    else :
        x_cut.append(int(temp[1]))

x_cut.sort()
y_cut.sort()

x_big = 0
for i in range(1, len(x_cut)) :
    val = x_cut[i] - x_cut[i - 1]
    if val > x_big :
        x_big = val
y_big = 0
for i in range(1, len(y_cut)) :
    val = y_cut[i] - y_cut[i - 1]
    if val > y_big :
        y_big = val

print(x_big * y_big)