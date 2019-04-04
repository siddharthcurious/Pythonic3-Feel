class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

def search(root, data):
    if not root:
        return None

    while root and root.val != data:
        if data < root.val:
            root = root.left
        else:
            root = root.right
    if root:
        return root.val
    return None

if __name__ == "__main__":

    root = TreeNode(20)
    root.left = TreeNode(15)
    root.right = TreeNode(30)
    root.left.left = TreeNode(10)
    root.right.right = TreeNode(35)
    root.right.left = TreeNode(28)
    root.left.right = TreeNode(18)

    # inorder(root)
    r1 = search(root, 20)
    r2 = search(root, 30)
    r3 = search(root, 28)
    r4 = search(root, 35)
    print(r1)
    print(r2)
    print(r3)
    print(r4)