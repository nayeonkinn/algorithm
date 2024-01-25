import sys

sys.stdin = open('input/2263.txt')  # 2 1 3
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# def to_preorder(inorder, postorder):  # 직접 리스트 넘겨주는 방식은 메모리 초과
#     if postorder:
#         root = postorder[-1]
#         print(root, end=" ")

#         mid = inorder.index(root)
#         to_preorder(inorder[:mid], postorder[:mid])
#         to_preorder(inorder[mid + 1:], postorder[mid:-1])

def to_preorder(il, ir, pl, pr):
    if il > ir or pl > pr:
        return
    
    root = postorder[pr]
    print(root, end=" ")

    mid = inorder_pos[root]
    cnt = mid - il  # 다음 트리 인덱스를 cnt 처리 없이 mid로 구분하는 경우 오답
    # 좌측 트리의 경우 두 리스트에서의 인덱스가 서로 동일하게 유지되지만 우측 트리의 경우 mid 값 때문에 인덱스가 달라짐
    # 따라서 inorder와 mid를 통해 다음 좌측 트리의 개수를 계산 후 postorder의 우측 트리 인덱스에 반영해야 함
    to_preorder(il, mid - 1, pl, pl + cnt - 1)
    to_preorder(mid + 1, ir, pl + cnt, pr - 1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorder_pos = {v: i for i, v in enumerate(inorder)}

# to_preorder(inorder, postorder)
to_preorder(0, n - 1, 0, n - 1)