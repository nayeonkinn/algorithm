import sys
sys.stdin = open('input/2536.txt')

m, n = map(int, input().split())
k = int(input())
bus_info, adj = {}, {}
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    bus_info[b] = ((x1, y1, x2, y2))
    adj[b] = []
sx, sy, dx, dy = map(int, input().split())

for bus in bus_info:
    print(bus)