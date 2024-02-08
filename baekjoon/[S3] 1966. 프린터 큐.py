import sys

sys.stdin = open('input/1966.txt')  # 1  2  5
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    docs = list(zip(map(int, input().split()), range(n)))

    cnt = 1
    while True:
        max_doc = max(docs)[0]
        doc, idx = docs.pop(0)

        if idx == m and doc == max_doc:
            print(cnt)
            break
        elif doc == max_doc:
            cnt += 1
        else:
            docs.append((doc, idx))