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

def root_to_leaf_sum(root, path, S):

    if not root:
        return

    path.append(root.val)
    if root.left is None and root.right is None:
        if sum(path) == S:
            print(path)
    root_to_leaf_sum(root.left, path, S)
    root_to_leaf_sum(root.right, path, S)
    path.pop()

if __name__ == "__main__":

    root = TreeNode(6)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.left.left = TreeNode(2)
    root.right.right = TreeNode(9)

    inorder(root)
    path = []
    root_to_leaf_sum(root, path, 23)