# 행렬을 활용한 피보나치 연산 https://st-lab.tistory.com/252

def multiply(m1, m2):
    return [[(m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % m, 
             (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % m], 
            [(m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % m, 
             (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % m]]

def power(matrix, n):
    if n == 1:
        return matrix

    result = power(matrix, n // 2)
    result = multiply(result, result)

    if n % 2:
        result = multiply(result, matrix)
    
    return result

n = int(input())
m = 1000000007

matrix = [[1, 1], [1, 0]]

print(power(matrix, n)[1][0])