K = int(input())

d = []
l = []
for i in range(6) :
    temp = input().split()
    d.append(int(temp[0]))
    l.append(int(temp[1]))

big = 1
for j in range(6) :
    if d.count(d[j]) == 1 :
        big *= l[j]

d2 = d * 2
small = 1
for k in range(9) :
    if d2[k] == d2[k + 2] and d2[k + 1] == d2[k + 3] :
        small *= l[(k + 1) % 6]
        small *= l[(k + 2) % 6]
        break

print(K * (big - small))