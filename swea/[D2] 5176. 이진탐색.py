import sys
sys.stdin = open('input/5176.txt')

def push(idx):
    global value
    if idx > N:
        return
    push(idx * 2)
    tree[idx] = value
    value += 1
    push(idx * 2 + 1)    

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    tree, value = [0] * (N + 1), 1
    push(1)
    print(f'#{t} {tree[1]} {tree[N // 2]}')
