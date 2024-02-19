import sys

sys.stdin = open('input/20040-1.txt')  # 0, 4
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:  # 루트가 같다는 건 사이클이 생긴다는 의미
        return -1
    elif a > b:
        parent[a] = b
    else:
        parent[b] = a

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    
    return parent[a]

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
answer = 0

for i in range(m):
    a, b = map(int, input().split())
    if union(a, b) == -1:
        answer = i + 1
        break

print(answer)