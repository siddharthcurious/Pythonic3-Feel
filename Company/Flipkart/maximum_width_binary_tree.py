class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sun():
    pass

if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.left.left = TreeNode(9)
    root.right.right.right = TreeNode(10)
    root.right.right.right.right = TreeNode(11)
    root.right.right.right.right.right = TreeNode(12)
    root.right.right.right.right.left = TreeNode(13)
    root.right.right.right.right.left.left = TreeNode(14)

    