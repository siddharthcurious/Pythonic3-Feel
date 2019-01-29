# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.sum = 0

        def range_sum(root):
            if not root:
                return
            range_sum(root.left)
            if root.val >= L and root.val <= R:
                self.sum = self.sum + root.val
            range_sum(root.right)
        range_sum(root)
        return self.sum

if __name__ == "__main__":

    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(25)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(15)
    root.right.left = TreeNode(23)
    root.right.right = TreeNode(27)
    root.right.right.right = TreeNode(30)

    obj = Solution()
    r = obj.rangeSumBST(root, 7, 23)
    print(r)
