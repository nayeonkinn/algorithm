import sys

sys.stdin = open('input/2179-3.txt')  # noon  noone, abcd  abc, abcc  ab
input = sys.stdin.readline

n = int(input())
words = sorted((input().strip(), i) for i in range(n))

prefix = 0
temp = set()  # 최대 접두사 길이 가진 단어들의 임시 집합
# 정렬했을 때는 붙어 있지 않지만 정답인 경우를 고려하기 위해 쌍으로 저장하지 않고 개별로 저장한 뒤 마지막에 순회하며 정답 여부 확인

for i in range(n - 1):
    a, idx_a = words[i]
    b, idx_b = words[i + 1]

    for idx in range(max(len(a), len(b))):
        if idx >= min(len(a), len(b)) or a[idx] != b[idx]:
            break

    if idx > prefix:
        prefix = idx
        temp = set()

    if idx == prefix:
        temp.add((idx_a, a))
        temp.add((idx_b, b))

temp = sorted(list(temp), key=lambda x: x[0])
_, s = temp[0]
for _, t in temp[1:]:
    if s[:prefix] == t[:prefix]:
        break
print(s)
print(t)