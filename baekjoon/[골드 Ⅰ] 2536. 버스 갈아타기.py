import sys
sys.stdin = open('input/2536.txt')

m, n = map(int, input().split())
k = int(input())
buses = {}
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    buses[b] = (x1, y1, x2, y2, True if x1 == x2 else False)

sx, sy, dx, dy = map(int, input().split())
start, dest = [], []
for i in range(1, k + 1):
    x1, y1, x2, y2, flag = buses[i]
    if flag:
        if sx == x1 and min(y1, y2) <= sy <= max(y1, y2):
            start.append(i)
        if dx == x1 and min(y1, y2) <= dy <= max(y1, y2):
            dest.append(i)
    else:
        if sy == y1 and min(x1, x2) <= sx <= max(x1, x2):
            start.append(i)
        if dy == y1 and min(x1, x2) <= dx <= max(x1, x2):
            dest.append(i)        

adj = [[] for _ in range(k + 1)]
for i in range(1, k):
    for j in range(i + 1, k + 1):
        flag = False
        Ax1, Ay1, Ax2, Ay2, Aflag = buses[i]
        Bx1, By1, Bx2, By2, Bflag = buses[j]

        if Ax1 > Ax2:
            Ax1, Ax2 = Ax2, Ax1
        if Ay1 > Ay2:
            Ay1, Ay2 = Ay2, Ay1
        if Bx1 > Bx2:
            Bx1, Bx2 = Bx2, Bx1
        if By1 > By2:
            By1, By2 = By2, By1

        if Aflag == True and Bflag == True:
            if Ax1 == Bx1 and (By1 <= Ay1 <= By2 or By1 <= Ay2 <= By2 or Ay1 <= By1 <= Ay2):
                flag = True
        elif Aflag == False and Bflag == False:
            if Ay1 == By1 and (Bx1 <= Ax1 <= Bx2 or Bx1 <= Ax2 <= Bx2 or Ax1 <= Bx1 <= Ax2):
                flag = True
        elif Aflag == True and Bflag == False:
            if Bx1 <= Ax1 <= Bx2 and Ay1 <= By1 <= Ay2:
                flag = True
        elif Aflag == False and Bflag == True:
            if Ax1 <= Bx1 <= Ax2 and By1 <= Ay1 <= By2:
                flag = True

        if flag:
            adj[i].append(j)
            adj[j].append(i)

answer = 5000
for s in start:
    visited = [False] * (k + 1)
    queue = [s]
    visited[s] = 1
    
    while queue:
        q = queue.pop(0)

        if q in dest:
            answer = min(visited[q], answer)
            break

        for e in adj[q]:
            if not visited[e]:
                queue.append(e)
                visited[e] = visited[q] + 1

print(answer)