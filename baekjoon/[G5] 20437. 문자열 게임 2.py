import sys

sys.stdin = open('input/20437-1.txt')  # 4 8  -1, 3 4

for _ in range(int(input())):
    w = input()
    k = int(input())

    pos = [[] for _ in range(26)]
    for i, c in enumerate(w):
        pos[ord(c) - 97].append(i)

    mn, mx = len(w), 0

    for p in pos:
        for i in range(len(p) - k + 1):
            mn = min(mn, p[i + k - 1] - p[i] + 1)
            mx = max(mx, p[i + k - 1] - p[i] + 1)
        
    print(f'{mn} {mx}' if mx else -1)