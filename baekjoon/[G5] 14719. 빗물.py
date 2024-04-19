import sys

sys.stdin = open('input/14719-1.txt')  # 5, 5, 0

h, w = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

# 1.
for i in range(1, h + 1):
    cnt = 0
    flag = False

    for j in range(w):
        if flag and arr[j] >= i:
            answer += cnt
            cnt = 0
        elif flag and arr[j] < i:
            cnt += 1
        elif not flag and arr[j] >= i:
            flag = True

# 2.
# for i in range(1, w - 1):
#     l_mx = max(arr[:i])
#     r_mx = max(arr[i+1:])

#     if arr[i] < (mn := min(l_mx, r_mx)):
#         answer += mn - arr[i]

print(answer)