# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        c = [0]
        p = [0]
        def inorder(root, k, c):
            if not root or c[0] > k:
                return
            inorder(root.left, k, c)
            c[0] = c[0] + 1
            if c[0] == k:
                p[0] = root.val
            inorder(root.right, k, c)
        inorder(root, k, c)
        return p[0]

if __name__ == "__main__":

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)
    root.left.right = TreeNode(4)

    s = Solution()
    k = 3
    r = s.kthSmallest(root, k)
    print(r)

