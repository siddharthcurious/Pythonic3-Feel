# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
import numpy

class Solution:

    def height(self, root):
        if not root:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        return 1+max(left, right)

    def printTree(self, root: TreeNode) -> List[List[str]]:

        result = []
        h = self.height(root)
        for _ in range(h):
            result.append([""]*(pow(2, h)-1))

        print(result)

        def pTree():
            pass


if __name__ == "__main__":

    obj = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    r  = obj.printTree(root)
    print(r)
