import sys
sys.stdin = open('input/15649-1.txt')


def permutation(numbers, visited):
    if len(numbers) == m:
        print(*numbers)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            permutation(numbers + [i + 1], visited)
            visited[i] = False


n, m = map(int, input().split())
visited = [False] * n
permutation([], visited)
