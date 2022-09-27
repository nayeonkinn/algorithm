import sys
sys.stdin = open('input/5205.txt')

def partition(l, r, nums):
    pivot = nums[index[l]]
    i, j = l, r
    while i <= j:
        while i <= j and nums[index[i]] <= pivot:
            i += 1
        while i <= j and nums[index[j]] >= pivot:
            j -= 1
        if i < j:
            index[i], index[j] = index[j], index[i]
    index[l], index[j] = index[j], index[l]
    return j

def qsort(l, r, nums):
    if l < r:
        s = partition(l, r, nums)
        qsort(l, s - 1, nums)
        qsort(s + 1, r, nums)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    index = [i for i in range(N)]
    qsort(0, N - 1, nums)
    print(f'#{tc} {nums[index[N // 2]]}')
