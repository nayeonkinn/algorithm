import sys
sys.stdin = open('input/15649-1.txt')


def backtracking(numbers):
    if len(numbers) == m:
        print(*numbers)
        return
    
    for i in range(n):
        backtracking(numbers + [i + 1])


n, m = map(int, input().split())
backtracking([])
