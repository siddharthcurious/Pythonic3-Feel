from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left == None and root.right == None:
            return True

        q = deque()
        q.append(root)
        v = 1
        flag = [1]
        while q:
            temp = q.popleft()
            if temp:
                q.append(temp.left)
                flag.append(2*v)
                q.append(temp.right)
                flag.append(2*v+1)
            v += 1
        if flag[-1] == len(flag):
            return True
        return False

if __name__ == "__main__":
    obj = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    r = obj.isCompleteTree(root)
    print(r)