class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right  = None

class BoundryTraversal:

    def left_boundry(self, root):
        if root:
            if(root.left):
                print(root.val)
                self.left_boundry(root.left)
            elif(root.right):
                print(root.val)
                self.left_boundry(root.right)

    def bottom_boundry(self, root):
        if not root:
            return
        self.bottom_boundry(root.left)
        if root.left is None and root.right is None:
            print(root.val)
        self.bottom_boundry(root.right)

    def right_boundry(self, root):
        if root:
            if(root.right):
                self.right_boundry(root.right)
                print(root.val)

            elif(root.left):
                self.right_boundry(root.left)
                print(root.val)

if __name__ == "__main__":


    root = TreeNode(20)
    root.left = TreeNode(15)
    root.right = TreeNode(25)
    root.left.left = TreeNode(13)
    root.left.right = TreeNode(17)
    root.right.left = TreeNode(23)
    root.right.right = TreeNode(27)

    obj = BoundryTraversal()
    obj.left_boundry(root)
    obj.bottom_boundry(root)
    obj.right_boundry(root)