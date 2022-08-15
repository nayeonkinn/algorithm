import sys
sys.stdin = open('input/7569-1.txt')  # -1, 4, 0

def ripe(box, d, r, red, green):
    h, n, m = r[0], r[1], r[2]
    for i in range(6):
        dh, dn, dm = h + d[i][0], n + d[i][1], m + d[i][2]
        if 0 <= dh < H and 0 <= dn < N and 0 <= dm < M and box[dh][dn][dm] == 0:
            box[dh][dn][dm] = 1
            red.append([dh, dn, dm])
            green -= 1
    return green

def tomato(box, H, N, M):
    green = 0
    red = []
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 0:
                    green += 1
                elif box[h][n][m] == 1:
                    red.append([h, n, m])
    if not green:
        return 0
    
    d = [[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0]]
    day = 0
    while red:
        day += 1
        redNext = []
        for r in red:
            green = ripe(box, d, r, redNext, green)
        if not green:
            return day
        red = redNext
    return -1

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for n in range(N)] for h in range(H)]
print(tomato(box, H, N, M))