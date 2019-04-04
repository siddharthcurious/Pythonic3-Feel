class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def iterative_preorder(root):
    if root == None:
        return

    

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

    iterative_preorder(root)