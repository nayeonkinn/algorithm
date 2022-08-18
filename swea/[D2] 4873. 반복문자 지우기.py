import sys
sys.stdin = open('input/4873.txt', 'r')

def len(word):
    cnt = 0
    for w in word:
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    s = input()
    stack = []
    for char in s:
        if not stack or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()

    print(f'#{tc} {len(stack)}')