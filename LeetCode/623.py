class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def addOneRow(self, root, v, depth):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if depth < 1:
            return root
        if depth == 1:
            temp = TreeNode(v)
            temp.left = root
            return temp

        q = deque()
        q.append((root, 1))

        while q:
            t, d = q.popleft()
            if d >= depth:
                break
            if d == depth-1:
                if t.left:
                    temp1 = t.left
                    t.left = TreeNode(v)
                    t.left.left = temp1
                else:
                    t.left = TreeNode(v)
                if t.right:
                    temp2 = t.right
                    t.right = TreeNode(v)
                    t.right.right = temp2
                else:
                    t.right = TreeNode(v)

            else:
                if t.left:
                    q.append((t.left, d+1))
                if t.right:
                    q.append((t.right, d+1))
        return root


if __name__ == "__main__":

    obj = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    v = 2
    d = 1
    obj.addOneRow(root, v, d)