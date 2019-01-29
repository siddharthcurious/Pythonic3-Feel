from collections import defaultdict

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

vmap = defaultdict(list)

def vertical_order(root, distance, vmap):
    if not root:
        return
    vertical_order(root.left, distance-1, vmap)
    vmap[distance].append(root.val)
    vertical_order(root.right, distance+1, vmap)

if __name__ == "__main__":

    root = TreeNode(20)
    root.left = TreeNode(15)
    root.right = TreeNode(25)
    root.left.left = TreeNode(13)
    root.left.right = TreeNode(17)
    root.right.left = TreeNode(23)
    root.right.right = TreeNode(27)

    inorder(root)
    vertical_order(root, 0, vmap)
    print(vmap)