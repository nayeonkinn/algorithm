import sys

sys.stdin = open('input/9527.txt')  # 21

def count(x):  # 1부터 x까지의 1의 개수 합 반환
    if x == 0:
        return 0
    
    n = len(bin(x)) - 3  # x가 i자리 이진수라면 n은 i - 1
    # x보다 작은 2의 제곱수 중 최댓값을 구할 때 사용
    # ex. x = 12 = 0b1100 (4자리 수) -> n = 3 -> 12보다 작은 2의 제곱수 중 최댓값은 2 ** n = 8

    return one[n] + x - 2 ** n + 1 + count(x - 2 ** n)
    # one[n]: 모든 i - 1자리 이진수의 1의 개수 합
    # x - 2 ** n + 1: 구해야 하는 i자리 이진수들의 맨 앞자리 1의 개수
    # count(x - 2 ** n): 구해야 하는 i자리 이진수들의 맨 앞자리 제외 나머지 자리의 1의 개수 = x에서 2 ** n을 뺀 수의 1의 개수

a, b = map(int, input().split())

one = [0] * 54  # one[i]: 0 ~ i자리 이진수의 1의 개수 합 (2**53 < 10**16 < 2**54)
for i in range(1, 54):
    one[i] = 2 ** (i - 1) + 2 * one[i - 1]

print(count(b) - count(a - 1))