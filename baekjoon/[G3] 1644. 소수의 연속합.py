import sys

sys.stdin = open('input/1644-1.txt')  # 0, 1, 3, 2

def get_prime():
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(2, n // i + 1):
                prime[i * j] = False

    prime = [i for i, v in enumerate(prime) if v]

    return prime

def consecutive():
    cnt = 0
    i, j = 0, 0

    prime = get_prime()
    total = prime[0]

    while 0 <= i <= j and i <= j < len(prime):
        if total == n:
            cnt += 1
        
        if total < n:
            j += 1
            if j == len(prime):
                break
            total += prime[j]
        else:
            total -= prime[i]
            i += 1
    
    return cnt

n = int(input())
if n == 1:
    print(0)
else:
    print(consecutive())