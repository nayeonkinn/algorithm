import sys
sys.stdin = open('input/15649-1.txt')


def combination(numbers, visited, now):
    if len(numbers) == m:
        print(*numbers)
        return
    
    for next in range(now, n):
        if not visited[next]:
            visited[next] = True
            combination(numbers + [next + 1], visited, next)
            visited[next] = False


n, m = map(int, input().split())
visited = [False] * n
combination([], visited, 0)
