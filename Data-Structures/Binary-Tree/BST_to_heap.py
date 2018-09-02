class TreeNode:
    def __init__(self, val):
        self.val = [val]
        self.left = None
        self.right = None

def bst_to_min_heap(root):

    travel = []
    def inorder(root):
        if root:
            inorder(root.left)
            travel.append(root.val)
            inorder(root.right)
    inorder(root)

    def perorder(root, i):
        if root:
            root.val[0] = travel[i]
            i = i + 1
            perorder(root.left, i)
            perorder(root.right, i)
    perorder(root, 0)

    travel = []
    inorder(root)
    print(travel)

if __name__ == "__main__":

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(6)

    bst_to_min_heap(root)