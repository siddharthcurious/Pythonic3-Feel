# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

import sys
class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min = sys.maxsize
        element = []

        if not root:
            return min

        def inorder(root):
            if root:
                inorder(root.left)
                element.append(root.val)
                inorder(root.right)
        inorder(root)
        for i in range(0, len(element)-1):
            d = abs(element[i] - element[i+1])
            if d < min:
                min = d
        return min


if __name__ == "__main__":

    s = Solution()

    root = TreeNode(20)
    root.left = TreeNode(15)
    root.right = TreeNode(25)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(17)

    r = s.getMinimumDifference(root)

    print(r)