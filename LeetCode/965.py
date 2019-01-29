# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def univalTree(root, store):
            if root == None:
                return
            store.add(root.val)
            univalTree(root.left, store)
            univalTree(root.right, store)
        store = set()
        univalTree(root, store)
        if len(store) > 1:
            return False
        return True

if __name__ == "__main__":

    s = Solution()

    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(2)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(2)

    r = s.isUnivalTree(root)
    print(r)

