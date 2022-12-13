S = input().upper()

maxcnt = 0
for s in set(S):
	cnt = S.count(s)
	if cnt > maxcnt:
		maxcnt = cnt
		result = s
	elif cnt == maxcnt:
		result = '?'

print(result)