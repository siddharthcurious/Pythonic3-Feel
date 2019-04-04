class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isIdentical(root1, root2):
    if root1 == None and root2 == None:
        return True
    elif root1 == None or root2 == None:
        return False
    elif root1.val == root2.val: #and root1.left.val == root2.left.val and root1.right.val == root2.right.val:
        return isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)
    return False

if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.right = TreeNode(5)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(4)

    r = isIdentical(root1, root2)
    print(r)