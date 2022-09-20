import sys
sys.stdin = open('input/1242.txt')

decode = {'211' : 0, '221' : 1, '122' : 2, '411' : 3, '132' : 4, '231' : 5, '114' : 6, '312' : 7, '213' : 8, '112' : 9}

T = int(input())
for t in range(1, T + 1):
    res = 0
    codes = []
    N, M = map(int, input().split())
    h_arr = set(input().strip().strip('0') for _ in range(N))
    h_arr.remove('')
    
    for h in h_arr:
        b = ''
        for i in h:
            sub_b = ''
            num = int(i, 16)
            for _ in range(4):
                sub_b = str(num % 2) + sub_b
                num //= 2
            b += sub_b
        
        b = b.strip('0')
        i = len(b) - 1
        code = []
        while i >= 0:
            c1 = c2 = c3 = 0
            while b[i] == '1':
                c3 += 1
                i -= 1
            while b[i] == '0':
                c2 += 1
                i -= 1
            while i >= 0 and b[i] == '1':
                c1 += 1
                i -= 1
            while i >= 0 and b[i] == '0':
                i -= 1
            mod = min(c1, c2, c3)
            code.append(decode[str(c1 // mod) + str(c2 // mod) + str(c3 // mod)])

            if len(code) == 8:
                if code not in codes:
                    val = 0
                    for j in range(8):
                        if j % 2:
                            val += 3 * code[j]
                        else:
                            val += code[j]
                    if not val % 10:
                        res += sum(code)
                    codes.append(code)
                code = []

    print(f'#{t} {res}')
