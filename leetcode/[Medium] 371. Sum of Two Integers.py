class Solution:
    def getSum(self, a: int, b: int) -> int:

        def convert(a):
            return a >= 0, bin(a)[2:] if a >= 0 else bin(a)[3:]
        
        def plus(aa, bb):
            flag, answer = False, ''
            for i in range(-1, -len(aa) - 1, -1):
                x, y = int(aa[i]), int(bb[i])
                if x & y:
                    if flag:
                        answer += '1'
                        flag = True
                    else:
                        answer += '0'
                        flag = True
                elif not (x | y):
                    if flag:
                        answer += '1'
                        flag = False
                    else:
                        answer += '0'
                        flag = False
                else:
                    if flag:
                        answer += '0'
                        flag = True
                    else:
                        answer += '1'
                        flag = False
            if flag:
                answer += '1'
            return int(answer[::-1], 2)

        def minus(aa, bb):
            flag, answer = False, ''
            for i in range(-1, -len(aa) - 1, -1):
                x, y = int(aa[i]), int(bb[i])
                if x & y:
                    if flag:
                        answer += '1'
                        flag = True
                    else:
                        answer += '0'
                        flag = False
                elif not (x | y):
                    if flag:
                        answer += '1'
                        flag = True
                    else:
                        answer += '0'
                        flag = False
                elif x and not y:
                    if flag:
                        answer += '0'
                        flag = False
                    else:
                        answer += '1'
                        flag = False
                elif not x and y:
                    if flag:
                        answer += '0'
                        flag = True
                    else:
                        answer += '1'
                        flag = True
            return int(answer[::-1], 2)

        if abs(a) < abs(b):
            a, b = b, a
        (sign_a, aa), (sign_b, bb) = convert(a), convert(b)
        
        diff = len(aa) - len(bb)
        if diff > 0:
            bb = '0' * diff + bb
        else:
            aa = '0' * -diff + aa
        
        if not (sign_a | sign_b) or (sign_a ^ sign_b and sign_b):
            sign = False
        else:
            sign = True

        if not (sign_a ^ sign_b):
            answer = plus(aa, bb)
        else:
            answer = minus(aa, bb)

        return answer if sign else -answer
