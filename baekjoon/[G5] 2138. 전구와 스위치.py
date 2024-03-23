import sys

sys.stdin = open('input/2138.txt')  # 3

def f(a):
    a = a[:]
    cnt = 0

    for i in range(1, n):
        if a[i - 1] != b[i - 1]:
            cnt += 1
            a[i - 1] = d[a[i - 1]]
            a[i] = d[a[i]]
            if i != n - 1:
                a[i + 1] = d[a[i + 1]]

    return cnt if a[-1] == b[-1] else 1e9

n = int(input())
a = list(input())
b = list(input())

# if a == b:  # 안 하는 게 더 빠르다
#     print(0)
#     exit()

d = {'1': '0', '0': '1'}

answer = f(a)
a[0] = d[a[0]]
a[1] = d[a[1]]
answer = min(answer, f(a) + 1)

print(answer if answer != 1e9 else -1)