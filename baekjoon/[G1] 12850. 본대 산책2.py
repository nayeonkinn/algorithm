# d = 100000000  # 261245548
d = int(input())

mod = 1000000007

def divide(arr, d):
    if d == 1:
        return arr
    elif d % 2 == 0:
        return divide(square(arr, arr), d // 2)
    else:
        return square(divide(arr, d - 1), arr)

def square(arr1, arr2):
    new_arr = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                new_arr[i][j] = (new_arr[i][j] + arr1[i][k] * arr2[k][j]) % mod
    return new_arr

arr = [[0, 1, 1, 0, 0, 0, 0, 0],
       [1, 0, 1, 1, 0, 0, 0, 0],
       [1, 1, 0, 1, 1, 0, 0, 0],
       [0, 1, 1, 0, 1, 1, 0, 0],
       [0, 0, 1, 1, 0, 1, 1, 0],
       [0, 0, 0, 1, 1, 0, 0, 1],
       [0, 0, 0, 0, 1, 0, 0, 1],
       [0, 0, 0, 0, 0, 1, 1, 0]]

print(divide(arr, d)[0][0])