import sys

sys.stdin = open('input/1100-1.txt')  # 1, 0, 32, 2

print(''.join(input()[i % 2::2] for i in range(8)).count('F'))