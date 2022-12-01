import sys
sys.stdin = open('input/2470.txt')  # -99 98

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

val, ans, l, r = 2000000000, '', 0, N - 1
while l < r:
    total = arr[l] + arr[r]
    if abs(total) < val:
        val = abs(total)
        ans = f'{arr[l]} {arr[r]}'

    if total == 0: break
    elif total > 0: r -= 1
    else: l += 1

print(ans)