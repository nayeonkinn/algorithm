import sys
sys.stdin = open('input/2011-1.txt') # 6, 89


# 분할정복 : 시간, 메모리 초과

# import sys
# sys.setrecursionlimit(10**6)

# def decode(code):
#     return chr(int(code) + 64)

# def compute(left, right):
#     result = set()
#     for l in left:
#         for r in right:
#             result.add(l + r)
#     return result

# def main(code):
#     if int(code) <= 9:
#         return {decode(code)}
#     elif int(code) <= 26:
#         return {decode(code), decode(code[0]) + decode(code[1])}

#     result = set()
#     for i in range(1, len(code)):
#         left = main(code[:i])
#         right = main(code[i:])
#         result |= compute(left, right)
#     return set(result)

# print(len(main(input())) % 1000000)


# 다이나믹 프로그래밍

def solve(code):
    if code[0] == '0': # 암호가 0으로 시작하는 건 암호가 잘못된 경우이므로 0을 리턴한다.
        return 0

    dp = [0] * (len(code) + 1) # (암호 두번째 자리부터) i - 2 값을 활용해서 계산할 것이므로 앞에 한 자리 여유를 준다.
    # 두번째 자리부터 계산하는 이유 : 첫번째 자리는 무조건 한가지 방법으로만 해석이 가능하기 때문에 계산할 필요가 없다.
    dp[0], dp[1] = 1, 1 # dp[0] = 1 : i - 2 계산을 위한 기본 값, dp[1] = 1 : 암호 첫번째 자리는 무조건 한가지로만 해석이 가능하다.
    for i in range(2, len(code) + 1): # 암호 두번째 자리부터 마지막 자리까지 순회한다.
        if int(code[i - 1]) > 0: # 현재 암호가 0이 아닌 수라면 이전과 동일한 경우의 수가 존재하므로
            dp[i] += dp[i - 1] # 현재 자리에 전 자리까지의 경우의 수를 더해준다.
        if 10 <= int(code[i - 2:i]) <= 26: # 이전과 현재를 묶은 암호가 알파벳으로 변환 가능한 범위 안에 있다면 그만큼의 경우의 수가 추가로 존재하므로
            dp[i] += dp[i - 2] # 현재 자리에 전 전 자리까지의 경우의 수를 더해준다.
    return dp[len(code)] % 1000000 # 마지막 자리까지의 경우의 수를 리턴한다.

print(solve(input()))
