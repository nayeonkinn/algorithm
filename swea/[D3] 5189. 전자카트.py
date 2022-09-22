import sys
sys.stdin = open('input/5189.txt')

def permutations(idx, way, battery):
    global answer
    if idx == N - 1:
        battery += table[way[-1]][0]
        answer = min(battery, answer)
        return

    for i in range(N):
        if i not in way:
            permutations(idx + 1, way + [i], battery + table[way[-1]][i])


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    answer = 100 * 10 * 10
    permutations(0, [0], 0)
    print(f'#{t} {answer}')