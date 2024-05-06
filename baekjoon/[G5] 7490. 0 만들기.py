import sys

sys.stdin = open('input/7490.txt')  # 1+2-3    1+2-3+4-5-6+7  1+2-3-4+5+6-7  1-2 3+4+5+6+7  1-2 3-4 5+6 7  1-2+3+4-5+6-7  1-2-3-4-5+6+7

def f(i, s):
    if i == n:
        if eval(s.replace(' ', '')) == 0:
            print(s)
        return
    
    for x in ' +-':
        f(i + 1, s + x + str(i + 1))

for _ in range(int(input())):
    n = int(input())

    f(1, '1')
    print()


# eval 함수 없이 구현

# def f(i, arr, s):
#     if i == n:
#         if sum(arr) == 0:
#             print(s)
#         return
    
#     if arr[-1] > 0:
#         f(i + 1, arr[:-1] + [arr[-1] * 10 + i + 1], s + ' ' + str(i + 1))
#     else:
#         f(i + 1, arr[:-1] + [arr[-1] * 10 - i - 1], s + ' ' + str(i + 1))
#     f(i + 1, arr + [i + 1], s + '+' + str(i + 1))
#     f(i + 1, arr + [- i - 1], s + '-' + str(i + 1))

# for _ in range(int(input())):
#     n = int(input())

#     f(1, [1], '1')
#     print()