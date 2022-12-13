# import sys
# sys.stdin = open("input.txt", "r")

N, K = list(map(int, input().split()))
ondo = [num for num in list(map(int, input().split()))]
total = [sum(ondo[:K])]
for i in range(N - K) :
    total.append(total[i] - ondo[i] + ondo[i + K])
print(max(total))