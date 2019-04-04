# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _search_path(self, root, target):
        if not root:
            return None

        data = []
        while root:
            pass

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """


if __name__ == "__main__":

    obj = Solution()

    root = TreeNode(20)
    root.left = TreeNode(15)
    root.right = TreeNode(30)
    root.left.left = TreeNode(10)
    root.right.right = TreeNode(35)
    root.right.left = TreeNode(28)
    root.left.right = TreeNode(18)
    root.right.left.right = TreeNode(29)
    root.right.left.left = TreeNode(25)

    r  = obj.lowestCommonAncestor(root, TreeNode(25), TreeNode(29))
    print(r)