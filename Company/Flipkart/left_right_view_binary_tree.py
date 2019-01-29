class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftview(root, level, max_level):
    if root is None:
        return

    if max_level[0] < level:
        print(root.data, end=" ")
        max_level[0] = level

    leftview(root.left, level+1, max_level)
    leftview(root.right, level+1, max_level)


def rightview(root, level, max_level):
    if root is None:
        return

    if max_level[0] < level:
        print(root.data, end=" ")
        max_level[0] = level

    rightview(root.right, level + 1, max_level)
    rightview(root.left, level+1, max_level)


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

    level = 0
    max_level = [-1]
    leftview(root, level, max_level)

    print()
    level = 0
    max_level = [-1]
    rightview(root, level, max_level)
