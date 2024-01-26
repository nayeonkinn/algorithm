import sys
from collections import defaultdict, deque

sys.stdin = open('input/9328.txt')  # 3  1  0
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    arr = ['.' * (w + 2)] + ['.' + input().strip() + '.' for _ in range(h)] + ['.' * (w + 2)]
    keys = {*input().strip()}

    q = deque([(0, 0)])
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    visited[0][0] = True

    wait = defaultdict(list)
    # 기존: 열 수 없는 문을 만난 경우 열쇠 저장 후 visited 초기화하여 다시 처음부터 탐색 (비효율적)
    # 개선: 열 수 없는 문을 wait에 모아 두고, 열쇠를 획득한 경우 한번에 큐에 삽입하여 탐색

    answer = 0

    while q:
        i, j = q.popleft()

        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj

            if ni < 0 or h + 2 <= ni or nj < 0 or w + 2 <= nj or visited[ni][nj] or arr[ni][nj] == '*':
                continue

            visited[ni][nj] = True  # 아래 if문에서 continue되더라도 다시 방문하지 않도록 먼저 방문 처리

            a = arr[ni][nj]
            if a.isupper() and a.lower() not in keys:  # 열 수 없는 문은 wait에 추가 후 continue
                wait[a.lower()].append((ni, nj))
                continue
            elif a.islower() and a not in keys:  # 새로운 열쇠 획득 시 열쇠 목록에 추가 및 wait 목록 큐에 삽입
                keys.add(a)
                q.extend(wait[a])
            elif a == '$':  # 문서 냠
                answer += 1
            
            q.append((ni, nj))  # continue되면 q에 삽입되지 않도록 뒤에서 삽입

    print(answer)