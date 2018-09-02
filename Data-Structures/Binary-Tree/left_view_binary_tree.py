class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):


    def leftView(self, root):

        def helper(root, level, mlevel):
            if not root:
                return

            if level > mlevel[0]:
                mlevel[0] = level
                print(root.val)
            helper(root.left, level+1, mlevel)
            helper(root.right, level+1, mlevel)

        max_level = [0]
        helper(root, 1, max_level)

if __name__ == "__main__":

    s = Solution()

    root = TreeNode(10)
    root.left = TreeNode(12)
    root.right = TreeNode(13)
    root.left.left = TreeNode(14)
    root.left.right = TreeNode(13)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(8)
    root.left.left.right = TreeNode(24)

    s.leftView(root)