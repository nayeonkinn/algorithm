import sys
input = sys.stdin.readline

N = int(input())
pillars = []
for i in range(N) :
    pillars.append(list(map(int, input().split())))

pillars.sort(key = lambda x : x[0])

max_p = pillars[0]
for pillar in pillars :
    if pillar[1] > max_p[1] :
        max_p = pillar

# max
result = max_p[1]

def roof(pillars, result) :
    before_l = 0
    before_h = 0
    for pillar in pillars :
        if pillar[1] >= before_h :
            result += abs(pillar[0] - before_l) * before_h
            before_l = pillar[0]
            before_h = pillar[1]
        if pillar == max_p :
            break
    return result

result = roof(pillars, result) # left
result = roof(pillars[::-1], result) # right

print(result)