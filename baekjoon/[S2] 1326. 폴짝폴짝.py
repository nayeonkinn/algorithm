import sys
sys.stdin = open('input/1326.txt')
input = sys.stdin.readline

def bfs():
    queue = [(a, 0)]
    visited = [False] * N
    visited[a] = True

    while queue:
        q, cnt = queue.pop(0)
        if q == b:
            return cnt

        for i in range(q, N, nums[q]):
            if not visited[i]:
                queue.append((i, cnt + 1))
                visited[i] = True
        for i in range(q, -1, -nums[q]):
            if not visited[i]:
                queue.append((i, cnt + 1))
                visited[i] = True

    return -1

N = int(input())
nums = list(map(int, input().split()))
a, b = map(lambda x: int(x) - 1, input().split())
print(bfs())
