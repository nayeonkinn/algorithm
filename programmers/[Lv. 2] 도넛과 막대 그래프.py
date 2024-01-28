from collections import defaultdict

def solution(edges):
    v_list = set()  # 정점 목록

    adj = defaultdict(list)  # 인접 리스트
    outdegree = defaultdict(int)  # 나가는 간선 개수
    indegree = defaultdict(int)  # 들어오는 간선 개수

    for a, b in edges:
        v_list.add(a)
        v_list.add(b)

        adj[a].append(b)
        outdegree[a] += 1
        indegree[b] += 1

    new_v = None  # 생성한 정점
    donut = stick = eight = 0  # 각 그래프의 개수

    for v in v_list:
        if outdegree[v] >= 2 and not indegree[v]:  # 생성한 정점의 특징: 나가는 간선 2개 이상, 들어오는 간선 없음
            new_v = v
    cnt = len(adj[new_v])  # 생성한 정점과 연결된 간선 수 = 그래프의 총 개수

    for a in adj[new_v]:
        indegree[a] -= 1  # 이후 판별을 위해 생성한 정점과 연결된 간선 삭제

    for v in v_list:
        if v == new_v:  # 생성한 정점인 경우 continue
            continue

        if indegree[v] == 0:  # 들어오는 간선이 없는 정점은 막대 그래프 당 하나만 존재
            stick += 1
        elif outdegree[v] == 2 and indegree[v] == 2:  # 나가는 간선 2개, 들어오는 간선 2개인 정점은 8자 그래프 당 하나만 존재
            eight += 1

    donut = cnt - stick - eight  # 그래프의 총 개수에서 막대 그래프와 8자 그래프의 개수 차감한 수가 도넛 그래프의 개수

    return [new_v, donut, stick, eight]