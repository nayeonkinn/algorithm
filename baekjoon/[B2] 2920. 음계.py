import sys
sys.stdin = open('input/2920-1.txt', 'r') # ascending, descending, mixed

c = list(map(int, input().split()))

if sorted(c) == c:
	print('ascending')
elif sorted(c, reverse = True) == c:
	print('descending')
else:
	print('mixed')