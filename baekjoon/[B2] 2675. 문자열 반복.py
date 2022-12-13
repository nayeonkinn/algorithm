import sys
sys.stdin = open('input/2675.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
	R, S = input().split()
	P = ''
	for s in S:
		P += s * int(R)
	print(P)