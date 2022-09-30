import sys
sys.stdin = open('input/5648.txt') # 24, 0, 6, 10

from collections import defaultdict

def move(atom):
    idx, answer = 0, 0

    while idx < 4000 and atom:
        atom2 = defaultdict(list)
        for i, j in atom:
            di, dj = delta[atom[(i, j)][0][0]]
            atom2[(di + i, dj + j)].extend(atom[i, j])
        
        for item in list(atom2.items()):
            if len(item[1]) > 1:
                for k in item[1]:
                    answer += k[1]
                del atom2[item[0]]
            if not -2000 < item[0][0] < 2000 or not -2000 < item[0][1] < 2000:
                del atom2[item[0]]

        idx += 1
        atom = atom2

    return answer

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atom = defaultdict(list)
    for _ in range(N):
        j, i, d, k = map(int, input().split())
        atom[(2 * i, 2 * j)] = [[d, k]]
    delta = ((1, 0), (-1, 0), (0, -1), (0, 1))
    print(f'#{tc} {move(atom)}')
