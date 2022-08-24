import sys
sys.stdin = open('input/1225.txt', 'r')

def encrypt(code):
    while True:
        for i in range(1, 6):
            code[0] -= i
            if code[0] < 1:
                return code[1:] + [0]
            code.append(code.pop(0))

for tc in range(1, 11):
    input()
    code = list(map(int, input().split()))
    print(f'#{tc}', *encrypt(code))