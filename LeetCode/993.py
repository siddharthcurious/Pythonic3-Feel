# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
    def getParent(root, val):
        if root == None:
            return None
        if root.left == None and root.right == None:
            return None
        if root.left:
            if root.left.val == val:
                return root.val
        if root.right:
            if root.right.val == val:
                return root.val
        return getParent(root.left, val)
        return getParent(root.right, val)

    hash = {}

    def depth(root, h):
        if not root:
            return
        hash.update({root.val: h})
        depth(root.left, h + 1)
        depth(root.right, h + 1)

    depth(root, 0)
    if hash[x] == hash[y]:
        if getParent(root, x) == getParent(root, y):
            return False
        else:
            return True
    return False

if __name__ == "__main__":

    s = Solution()

    root = TreeNode(10)
    root.left = TreeNode(11)
    root.right = TreeNode(13)
    root.left.left = TreeNode(15)
    root.left.right = TreeNode(17)


    root = TreeNode(1)


    r = s.isCousins(root, 15, 17)
    print(r)
