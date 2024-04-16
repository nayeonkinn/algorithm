import sys

sys.stdin = open('input/24337-1.txt')  # 1 2 3, 1, 9 1 8 7 6 5 4 3 2 1

n, a, b = map(int, input().split())

if a + b - 1 > n:
    print(-1)
    exit()

answer = [i for i in range(1, a)] + [max(a, b)] + [i for i in range(b - 1, 0, -1)]

print(answer[0], *[1 for _ in range(n - len(answer))], *answer[1:])