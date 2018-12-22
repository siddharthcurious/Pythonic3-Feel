from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def level_order(root):
    q = deque()
    q.append(root)

    while q:
        temp = q.popleft()
        print(temp.val, end=" ")

        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

if __name__ == "__main__":

    root = TreeNode(10)
    root.left = TreeNode(11)
    root.right = TreeNode(12)
    root.left.left = TreeNode(13)
    root.left.right = TreeNode(15)
    root.right.right = TreeNode(20)
    root.right.left = TreeNode(34)

    level_order(root)

