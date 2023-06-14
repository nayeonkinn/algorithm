import sys
sys.stdin = open('input/15649-1.txt')


def solution(numbers, now):
    if len(numbers) == m:
        print(*numbers)
        return
    
    for i in range(now, n):
        solution(numbers + [i + 1], i)


n, m = map(int, input().split())
solution([], 0)
