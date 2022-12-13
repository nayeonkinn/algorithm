l = [int(n[::-1]) for n in input().split()]
print(l[0]) if l[0] > l[1] else print(l[1])