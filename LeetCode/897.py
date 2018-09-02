# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        inorder_travel = []
        self.inorder(root, inorder_travel)

        root1 = current = TreeNode(-1)

        for v in inorder_travel:
            current.right = TreeNode(v)
            current = current.right
        return root1.right

    def inorder(self, root, output):
        if not root:
            return

        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)



