import sys
sys.stdin = open('input/3143.txt', 'r')

def len(word):
    cnt = 0
    for w in word:
        cnt += 1
    return cnt

T = int(input())
for tc in range(T):
    A, B = input().split()
    print(f'#{tc + 1} {len(A) - A.count(B) * (len(B) - 1)}')