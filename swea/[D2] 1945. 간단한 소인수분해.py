import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
div = [2, 3, 5, 7, 11]

for t in range(T) :
    ans = [0] * 5
    num = int(input())

    for i in range(5) :
        while num % div[i] == 0 :
            ans[i] += 1
            num /= div[i]

    print(f'#{t + 1} {" ".join(map(str, ans))}')