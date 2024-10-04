import sys

sys.stdin = open('input/1159-2.txt')  # bk, PREDAJA
input = sys.stdin.readline

N = int(input())

dic = {i: 0 for i in range(97, 123)}

for _ in range(N):
    name = input().strip()
    dic[ord(name[0])] += 1

answer = list(map(chr, filter(lambda x: dic[x] > 4, dic.keys())))

print(''.join(answer) if answer else 'PREDAJA')