T = int(input())
for t in range(T) :
    word = str(input())
    if word == word[::-1] :
        result = 1
    else :
        result = 0
    print("#%d %d" % (t + 1, result))