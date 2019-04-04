class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        q = deque()
        q.append(root)
        q.append("M")

        result = []
        level = []
        while q.__len__() >= 1:
            t = q.popleft()
            if t != "M" and t != None:
                level.append(t.val)

            if t == "M":
                if level:
                    result.append(level)
                if q.__len__() == 0:
                    break
                q.append("M")
                level = []

            if isinstance(t, Node):
                if t.children:
                    for ch in t.children:
                        if ch != []:
                            q.append(ch)
        return result

if __name__ == "__main__":

    root = Node(1, [0]*3)
    root.children[0] = Node(2, None)
    root.children[1] = Node(3, None)
    root.children[2] = Node(4, None)

    obj = Solution()
    r = obj.levelOrder(root)
    print(r)


