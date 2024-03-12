import sys

sys.stdin = open('input/12919-1.txt')  # 1, 1, 0

def recur(word):
    if word == s:
        print(1)
        exit()
    elif len(word) == len(s):
        return

    if word.endswith('A'):
        recur(word[:-1])
    
    if word.startswith('B'):
        recur(word[1:][::-1])
    
s = input()
t = input()

recur(t)

print(0)