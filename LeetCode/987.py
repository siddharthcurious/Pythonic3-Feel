# Definition for a binary tree node.
from typing import List
from collections import defaultdict
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        data = defaultdict(list)

        def vertical(root, v):
            if not root:
                return []
            data[v].append(root.val)
            vertical(root.left, v-1)
            vertical(root.right, v+1)
        vertical(root, 0)
        r = []
        for k, v in data.items():
            r.append(v)
        return r

if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.right = TreeNode(5)

    obj = Solution()
    r = obj.verticalTraversal(root1)
    print(r)
