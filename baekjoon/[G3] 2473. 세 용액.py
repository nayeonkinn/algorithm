import sys

sys.stdin = open('input/2473-1.txt')  # -97 -2 98, -6 -3 -2
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))

min_value = float('inf')

for i in range(n - 2):
    j, k = i + 1, n - 1

    while j < k:
        value = arr[i] + arr[j] + arr[k]
        if abs(value) < min_value:
            min_value = abs(value)
            answer = (arr[i], arr[j], arr[k])

        if value == 0:
            print(*answer)
            exit()
        elif value < 0:
            j += 1
        else:
            k -= 1

print(*answer)