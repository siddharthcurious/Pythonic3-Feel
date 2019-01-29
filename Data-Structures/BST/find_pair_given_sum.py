class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.inorder_set = set()

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)

    def find_pair_given_sum(self, root, num):
        if not root:
            return False

        if self.find_pair_given_sum(root.left, num):
            return True
        k = num - root.val
        if k in self.inorder_set:
            return True
        else:
            self.inorder_set.add(root.val)

        return self.find_pair_given_sum(root.right, num)

if __name__ == "__main__":

    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(25)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(15)
    root.right.left = TreeNode(23)
    root.right.right = TreeNode(27)

    obj = BST()
    obj.inorder(root)
    r = obj.find_pair_given_sum(root, 23)
    print(r)


