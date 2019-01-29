class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder_recursive(root):
    if not root:
        return
    stack = []
    stack.append(root)

    while(len(stack) > 0):
        node = stack.pop()
        print(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

if __name__ == "__main__":

    root = TreeNode(10)
    root.left = TreeNode(11)
    root.right = TreeNode(12)
    root.left.left = TreeNode(13)
    root.left.right = TreeNode(15)
    root.right.left = TreeNode(16)
    root.right.right = TreeNode(17)

    preorder_recursive(root)
