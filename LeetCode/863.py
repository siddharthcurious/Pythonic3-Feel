# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        result = []
        def distance_tree(root, d):
            if not root:
                return
            distance_tree(root.left, d+1)
            print(root.val, d)
            distance_tree(root.right, d+1)

        distance_tree(root, 0)

if __name__ == "__main__":


    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    obj = Solution()
    target = 5
    K = 2
    obj.distanceK(root, target, K)

