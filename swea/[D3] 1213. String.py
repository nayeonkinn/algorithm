# import sys
# sys.stdin = open('input.txt', 'r', encoding = 'UTF8')

for T in range(1, 11):
    input()
    p = input()
    t = input()

    p_len = len(p)
    t_len = len(t)

    p_i = t_i = cnt = 0
    while t_i < t_len:
        if t[t_i] != p[p_i]:
            t_i -= p_i
            p_i = -1

        t_i += 1
        p_i += 1

        if p_i == p_len:
            cnt += 1
            t_i -= p_i - 1
            p_i = 0

    print(f'#{T} {cnt}')