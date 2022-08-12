# import sys
# sys.stdin = open('input.txt', 'r')

numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for t in range(T):
    n = int(input().split()[1])
    arr = input().split()
    sorted_arr = [[] for _ in range(10)]
    for a in arr:
        for i in range(10):
            if a == numbers[i]:
                sorted_arr[i].append(a)
    print(f'#{t + 1}')
    for i in range(10):
        print(*(sorted_arr[i]))