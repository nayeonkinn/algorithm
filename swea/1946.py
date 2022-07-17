T = int(input())
for t in range(T) :
    N = int(input())
    text = ""
    for n in range(N) :
        C, K = input().split()
        text += C * int(K)
    print("#%d" % (t + 1))
    for i in range(len(text)) :
        if i % 10 == 9 :
            print(text[i])
        else :
            print(text[i], end = "")
    print()