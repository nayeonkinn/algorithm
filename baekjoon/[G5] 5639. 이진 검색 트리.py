import sys
sys.stdin = open('input/5639.txt')  # 5 28 24 45 30 60 52 98 50
sys.setrecursionlimit(10**9)


def postorder(root, end):
    if root > end:
        return
    
    start = end + 1
    for i in range(root + 1, end + 1):
        if nodes[i] > nodes[root]:
            start = i
            break

    postorder(root + 1, start - 1)
    postorder(start, end)

    print(nodes[root])


nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:
        break

postorder(0, len(nodes) - 1)
