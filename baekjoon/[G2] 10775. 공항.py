import sys

sys.stdin = open('input/10775-1.txt')  # 2, 3
input = sys.stdin.readline

def find(x):
    if gate[x] != x:
        gate[x] = find(gate[x])

    return gate[x]

G = int(input())
P = int(input())

gate = [i for i in range(G + 1)]
answer = 0

for _ in range(P):
    g = int(input())

    num = find(g)
    if not num:  # 0번 게이트 연결된다면 더 이상 도킹할 수 없다는 의미
        break
    
    # num번에 연결된 게이트로 도킹 완료
    # 이후 num번 게이트로 다시 도킹 시도한다면, 이미 자리가 찼으므로 그 전 게이트인 num - 1번에 연결된 게이트로 도킹되도록 union 수행
    gate[num] = gate[num - 1]
    answer += 1

print(answer)