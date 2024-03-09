import sys

sys.stdin = open('input/1541-1.txt')  # -35, 100, 0

exp = input().split('-')  # 값을 최소로 만들기 위해서는 뺄셈을 기준으로 식을 나눠야 함

for i in range(len(exp)):
    exp[i] = sum(map(int, exp[i].split('+')))

print(exp[0] - sum(exp[1:]))