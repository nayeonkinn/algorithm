def f(n):
    return int(n) ** 2

N = list(map(f, input().split()))
print(sum(N) % 10)

# print(sum([int(n) ** 2 for n in input().split()]) % 10)