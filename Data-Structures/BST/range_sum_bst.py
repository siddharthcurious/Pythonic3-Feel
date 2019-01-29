class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.total = 0

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)

    def range_sum(self, min, max):
        if not root:
            return
        path.append(root.val)
        if root.left is None and root.right  is None:
            print(path)
        self.print_all_paths(root.left, path)
        self.print_all_paths(root.right, path)
        path.pop()

if __name__ == "__main__":

    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(25)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(15)
    root.right.left = TreeNode(23)
    root.right.right = TreeNode(27)
    root.right.right.right = TreeNode(30)

    obj = BST()
    obj.print_all_paths(root, [])


