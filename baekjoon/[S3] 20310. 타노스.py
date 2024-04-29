import sys

sys.stdin = open('input/20310-1.txt')  # 01, 001

s = list(input())

zero = s.count('0') // 2
one = s.count('1') // 2

i, cnt = 0, 0
while cnt < one:
    if s[i] == '1':
        cnt += 1
        s[i] = ''
    i += 1

i, cnt = len(s) - 1, 0
while cnt < zero:
    if s[i] == '0':
        cnt += 1
        s[i] = ''
    i -= 1

print(''.join(s))