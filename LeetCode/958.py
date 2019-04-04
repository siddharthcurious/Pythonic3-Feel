# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def height(self, root):
        if not root:
            return 0
        else:
            l = self.height(root.left)
            r = self.height(root.right)
            return 1 + max(l, r)
    def isCompleteTree(self, root: TreeNode) -> bool:
        h = self.height(root)
        total = pow(2, 3) - 1
        data = [0] * total

 


if __name__ == "__main__":

    obj = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    obj.isCompleteTree(root)
