from collections import deque
import sys

sys.stdin = open('input/10845.txt')  # 1  2  2  0  1  2  -1  0  1  -1  0  3
input = sys.stdin.readline

q = deque()

for _ in range(int(input())):
    cmd = input().strip()

    if cmd[:4] == 'push':
        q.append(cmd.split()[-1])
    elif cmd == 'pop':
        print(q.popleft() if q else -1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        print(0 if q else 1)
    elif cmd == 'front':
        print(q[0] if q else -1)
    elif cmd == 'back':
        print(q[-1] if q else -1)