# import sys
# sys.stdin = open('input.txt', 'r')

first = int(input())
maxcnt = 0

for second in range(first // 2, first + 1) :
    cnt = 2

    one = first
    two = second
    next = one - two

    arr = [one, two]

    while next >= 0 :
        arr.append(next)
        cnt += 1
        one = two
        two = next
        next = one - two
        if cnt > maxcnt :
            maxcnt = cnt
            maxarr = arr

print(maxcnt)
print(" ".join(map(str, maxarr)))