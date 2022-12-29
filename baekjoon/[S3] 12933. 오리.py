import sys
sys.stdin = open('input/12933-1.txt') # 2, -1, 1, 10, 3, -1

def solution():
    dic = {0: 'q', 1: 'u', 2: 'a', 3: 'c', 4: 'k'}
    quack = input()
    answer, idx = 0, 0
    visited = [False] * len(quack)
    while not all(visited):
        flag = False
        for i in range(len(quack)):
            if not visited[i]:
                if quack[i] == dic[idx]:
                    flag = True
                    visited[i] = True
                    idx = (idx + 1) % 5
        if flag and idx == 0:
            answer += 1
        else:
            return -1
    return answer

print(solution())
