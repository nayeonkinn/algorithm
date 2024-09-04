import sys

sys.stdin = open('input/1864.txt')  # 158  1984  -47  4
input = sys.stdin.readline

sign = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}

while (octopus := input().strip()) != '#':
    answer = 0
    for idx, char in enumerate(octopus[::-1]):
        answer += 8 ** idx * sign[char]
    print(answer)