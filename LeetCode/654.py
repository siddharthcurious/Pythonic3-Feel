# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        rval = max(nums)
        index = nums.index(rval)
        root = TreeNode(rval)
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end= " ")
            self.inorder(root.right)


if __name__ == "__main__":

    s = Solution()
    nums = [3,2,1,6,0,5]
    root = s.constructMaximumBinaryTree(nums)
    s.inorder(root)



