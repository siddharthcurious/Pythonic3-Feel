from collections import deque
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0

def bottom_view(root):
    if root is None:
        return []

    result = {}
    hd = 0
    q = deque()
    q.append(root)

    while q:
        temp = q.popleft()
        hd = temp.hd
        result[hd] = temp.data

        if temp.left:
            temp.left.hd = hd - 1
            q.append(temp.left)
        if temp.right:
            temp.right.hd = hd + 1
            q.append(temp.right)
    return list(result.values())

if __name__ == "__main__":

    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(25)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)

    r = bottom_view(root)
    print(r)