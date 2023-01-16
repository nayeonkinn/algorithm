import sys
sys.stdin = open('input/20529.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    mbti = input().split()
    print(mbti)

    for i in range(N << 2):
        cnt = 0
        for j in range(N):
            if i & (1 << j):    
                cnt += 1
        if cnt == 3:
            for k in range(N):
                if len(bin(i)) > 2 + k and bin(i)[2 + k] == '1':
                    print(3)
            print(bin(i))