from collections import deque
import sys

sys.stdin = open('input/2638.txt')  # 4
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
air, candidate, melt = deque([(0, 0)]), [], []
visited = [[False] * M for _ in range(N)]
d = ((1, 0), (-1, 0), (0, 1), (0, -1))

while True:
    while air:  # 외부 공기 방문 처리
        i, j = air.popleft()

        for di, dj in d:
            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = True
                if arr[ni][nj]:  # 치즈가 있으면
                    candidate.append((ni, nj))  # 후보 리스트에 추가
                else:  # 치즈가 없으면
                    air.append((ni, nj))  # 외부 공기 리스트에 추가
    
    if not candidate:  # 치즈가 없으면
        break  # 중단

    for i, j in candidate:  # 후보 리스트 순회하며 녹는 대상인지 확인
        cnt = 0

        for di, dj in d:
            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj] and visited[ni][nj]:  # 치즈가 없고 방문한 적이 있으면(== 외부 공기면)
                cnt += 1

        if cnt >= 2:  # 외부 공기에 2개 이상 닿으면
            melt.append((i, j))  # 녹는 치즈 리스트에 추가
        else:  # 외부 공기에 2개 이상 닿지 않으면
            visited[i][j] = False  # 해당 치즈 자리가 다시 후보 리스트에 추가될 수 있도록 방문 취소

    for i, j in melt:  # 녹는 치즈 리스트 순회하며 치즈 녹임
        arr[i][j] = 0

    answer += 1

    air, candidate, melt = deque(melt), [], []  # 녹은 치즈는 외부 공기가 되었으니, 다시 주변 탐색하며 새로운 외부 공기(== 내부 공기였던 부분)와 다음으로 녹을 치즈 후보를 찾을 수 있도록 외부 공기 리스트로 변환

print(answer)