a, b = 24, 18  # 6  72
# a, b = map(int, input().split())

def gcd(a, b):
    while a % b and a:
        r = a % b
        a, b = b, r
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))