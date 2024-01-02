import sys
sys.stdin = open('input/1865.txt')  # NO YES
input = sys.stdin.readline

def bf():
    costs = [1e9] * (n + 1)
    costs[1] = 0  # 사이클의 유무만 확인하기 때문에 시작지점 무관

    for i in range(n):
        for s, e, t in graph:
            if costs[e] > costs[s] + t:  # 최소 비용 계산하지 않기 때문에 (사이클의 존재 유무만 확인) costs[s] != 1e9 조건 삭제
                costs[e] = costs[s] + t
                if i == n - 1:  # 이미 n - 1번 진행하고, n번째 진행함에도 갱신이 된다는 건 사이클이 존재한다는 것
                    return True

    return False

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = []

    for i in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))

    for i in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))

    if bf():
        print('YES')
    else:
        print('NO')