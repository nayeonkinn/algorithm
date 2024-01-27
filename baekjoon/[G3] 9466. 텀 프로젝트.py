import sys

sys.stdin = open('input/9466.txt')  # 3  0
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

t = int(input())

def dfs(i):
    global answer

    visited[i] = True

    j = team[i]  # 다음 방문 대상
    
    if not visited[j]:  # 방문한 적이 없다면
        dfs(j)  # 방문
    elif not done[j]:  # 방문한 적은 있지만 완료되지 않았다면 사이클 발생하여 팀이 구성되었다는 의미
        while j != i:  # 역추적하여 팀원 수 계산
            answer -= 1
            j = team[j]
        answer -= 1  # 자기 자신 포함
        # 탐색 중간부터 사이클 존재할 수 있기 때문에(ex. 1 - 3 - 2 - 4 - 3) 단순 카운트 처리 불가
    
    done[i] = True

for _ in range(t):
    n = int(input())
    team = list(map(lambda x: int(x) - 1, input().split()))

    visited = [False] * n  # 단순 방문 여부
    done = [False] * n  # 완료 여부 (더 이상 방문하지 않아도 되는가)

    answer = n

    for i in range(n):
        if not visited[i]:  # 방문한 적이 없다면
            dfs(i)  # 방문
    
    print(answer)