class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isIsomorphism(root1, root2):
    if root1 == None and root2 == None:
        return True
    elif root1 == None or root2 == None:
        return False
    elif root1.val == root2.val:
        return (isIsomorphism(root1.left, root2.left) and isIsomorphism(root1.right, root2.right)) or \
               (isIsomorphism(root1.left, root2.right) and isIsomorphism(root1.right, root2.left))
    return False

if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(8)

    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(5)
    root2.left.right = TreeNode(6)
    root2.right.right.left = TreeNode(8)
    root2.right.right.right = TreeNode(7)

    r = isIsomorphism(root1, root2)
    print(r)