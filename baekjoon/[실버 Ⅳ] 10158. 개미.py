# import sys
# sys.stdin = open('input1.txt', 'r') # 0 1
# # sys.stdin = open('input2.txt', 'r') # 3 1

col, row = map(int, input().split())
q, p = map(int, input().split())
t = int(input())

# 시 간 초 과 #

# dp = 1
# dq = 1

# for hour in range(t) :
#     if p + dp > row or p + dp < 0 :
#         dp *= -1
#     if q + dq > col or q + dq < 0 :
#         dq *= -1
#     p += dp
#     q += dq

p = (p + t) % (2 * row)
q = (q + t) % (2 * col)

if p > row :
    p -= 2 * (p - row)
if q > col :
    q -= 2 * (q - col)

print(q, p)