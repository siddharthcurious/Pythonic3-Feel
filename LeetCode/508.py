# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import Counter
class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result

        def sumTree(root):

            if root is None:
                return 0
            else:
                return sumTree(root.left) + root.val + sumTree(root.right)

        def helper(root):
            if root:
                helper(root.left)
                result.append(sumTree(root))
                helper(root.right)
        helper(root)


        rcounter = Counter(result)
        vs = set(rcounter.values())
        if len(vs) == 1:
            return list(set(rcounter.keys()))

        r = []
        sorted_result = sorted(rcounter.items(), key=lambda x: x[1], reverse=True)
        for i in range(len(sorted_result)-1):
            r.append(sorted_result[i][0])
            if sorted_result[i][1] > sorted_result[i+1][1]:
                return r


if __name__ == "__main__":

    s = Solution()

    """
    root = TreeNode(10)
    root.left = TreeNode(3)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(-1)
    root.right.right = TreeNode(10)
    """

    root = TreeNode(0)
    root.left = TreeNode(-1)
    #root.right = TreeNode(-5)

    r = s.findFrequentTreeSum(root)
    print(r)