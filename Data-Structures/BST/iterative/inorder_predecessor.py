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

def last_rightturn(root, data):
    if not root:
        return None
    t = None
    while root and root.val != data:
        if data < root.val:
            root = root.left
        else:
            t = root
            root = root.right
    return t

def find_rightmost(root):
    if not root:
        return None
    t = None
    if root.right == None:
        return root
    else:
        while root:
            t = root
            root = root.right
    return t

def search(root, data):
    if not root:
        return None
    while root and root.val != data:
        if data < root.val:
            root = root.left
        else:
            root = root.right
    if root:
        return root

def inorder_predecessor(root, data):
    if not root:
        return None
    if root.left == None and root.right == None:
        return root.val

    target = search(root, data)
    if not target:
        return None
    elif target.left:
        return find_rightmost(target.left)
    elif not target.left:
        return last_rightturn(root, data)

if __name__ == "__main__":

    root = TreeNode(20)
    root.left = TreeNode(15)
    root.right = TreeNode(30)
    root.left.left = TreeNode(10)
    root.right.right = TreeNode(35)
    root.right.left = TreeNode(28)
    root.left.right = TreeNode(18)
    root.right.left.right = TreeNode(29)
    root.right.left.left = TreeNode(25)

    inorder(root)
    print()
    r = inorder_predecessor(root, 25)
    print(r.val)


