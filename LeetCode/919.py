# Definition for a binary tree node.

from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root

    def insert(self, v: int) -> int:
        if self.root == None:
            self.root = TreeNode(v)
            return v

        q = deque()
        q.append(self.root)
        while q:
            t = q.popleft()
            if t.left:
                q.append(t.left)
            else:
                t.left = TreeNode(v)
                return v
            if t.right:
                q.append(t.right)
            else:
                t.right = TreeNode(v)
                return v

    def get_root(self) -> TreeNode:
        return self.root

if __name__ == "__main__":

    root = TreeNode(1)
    obj = CBTInserter(root)
    v = 2
    param_1 = obj.insert(v)
    print(param_1)
    param_2 = obj.get_root()
    print(param_2.left.val)