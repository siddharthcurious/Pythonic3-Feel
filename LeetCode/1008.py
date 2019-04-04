# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        node = TreeNode(preorder[0])
        split = 1

        while split < len(preorder) and preorder[0] > preorder[split]:
            split += 1

        node.left = self.bstFromPreorder(preorder[1:split])
        node.right = self.bstFromPreorder(preorder[split:])
        return node



if __name__ == "__main__":

    obj = Solution()
    preorder = [8, 5, 1, 7, 10, 12]
    obj.bstFromPreorder(preorder)
