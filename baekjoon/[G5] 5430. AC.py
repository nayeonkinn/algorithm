from collections import deque
import sys

sys.stdin = open('input/5430.txt')  # [2,1]  error  [1,2,3,5,8]  error
input = sys.stdin.readline

def ac(arr):
    r = False

    for x in p:
        if x == 'R':
            r = not r
        else:  # x == 'D'
            if not arr:
                return 'error'
            elif r:
                arr.pop()
            else:
                arr.popleft()
    
    return('[' + ','.join(reversed(arr) if r else arr) + ']')
    
for _ in range(int(input())):
    p = input().strip().replace('RR','')
    n = int(input())
    arr = deque(input()[1:-2].split(','))
    
    print(ac(arr if n else []))