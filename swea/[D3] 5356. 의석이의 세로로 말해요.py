import sys
sys.stdin = open('input/5356.txt', 'r')

T = int(input())
for t in range(T):
    print(f'#{t + 1} ', end = '')
    words = [input() for _ in range(5)]

    for i in range(15):
        for word in words:
            if i < len(word):
                print(word[i], end = '')
    print()