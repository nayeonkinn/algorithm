import sys
sys.stdin = open('input/15654-1.txt')


def solution(numbers, visited):
    if len(numbers) == m:
        print(*numbers)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            solution(numbers + [arr[i]], visited)
            visited[i] = False


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * n
solution([], visited)
