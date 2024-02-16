import sys

sys.stdin = open('input/4949.txt')  # yes  yes  no  no  no  yes  yes
input = sys.stdin.readline

pair = {')': '(', ']': '['}

while (s := input().rstrip('\n')) != '.':
    answer = 'yes'

    stack = []

    for char in s.strip():
        if char in ('(', '['):
            stack.append(char)

        elif char in (')', ']'):
            if stack and stack.pop() == pair[char]:
                pass
            else:
                answer = 'no'
                break
    
    if stack:
        answer = 'no'

    print(answer)