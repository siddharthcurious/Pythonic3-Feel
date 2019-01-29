# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def sum_of_left_leaves(root, is_left, sum):

            if root is None:
                return

            if root.left is None and root.right is None and is_left == True:
                sum[0] = sum[0] + root.val
            sum_of_left_leaves(root.left, 1, sum)
            sum_of_left_leaves(root.right, 0, sum)

        sum = [0]
        sum_of_left_leaves(root, 0, sum)
        return sum[0]

if __name__ == "__main__":

    s = Solution()
    s.sumOfLeftLeaves()
