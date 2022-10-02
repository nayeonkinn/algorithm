# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        queue = [root]
        data = []
        
        while queue:
            node = queue.pop(0)
            if node:
                data.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                data.append('-1001')
                
        return ' '.join(data)

    def deserialize(self, data):
        if data == '-1001':
            return
        
        data = list(map(int, data.split()))
        root = TreeNode(data[0])
        queue = [root]
        idx = 1

        while queue:
            node = queue.pop(0)
            if data[idx] != -1001:
                node.left = TreeNode(data[idx])
                queue.append(node.left)
            if data[idx + 1] != -1001:
                node.right = TreeNode(data[idx + 1])
                queue.append(node.right)
            idx += 2

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))