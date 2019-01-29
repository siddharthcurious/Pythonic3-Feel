# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """



if __name__ == "__main__":


    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.right = TreeNode(15)
    root1.left.left = TreeNode(2)

    root2 = TreeNode(10)
    root2.left = TreeNode(15)
    root2.right = TreeNode(5)
    root2.right.left = TreeNode(2)

    obj = Solution()
    r = obj.flipEquiv(root1, root2)
    print(r)



