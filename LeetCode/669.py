# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        self.trimBST(root.left, L, R)
        self.trimBST(root.right, L, R)

        if root.val < L:
            del root


if __name__ == "__main__":

    obj = Solution()

    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(30)
    root.right.right = TreeNode(40)
    root.left.left = TreeNode(5)

    obj.trimBST(root, 5, 30)

