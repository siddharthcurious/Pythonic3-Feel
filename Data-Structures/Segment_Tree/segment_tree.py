from collections import deque
from collections import defaultdict
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class SegmentTree:

    def __init__(self, nums):

        def createTree(nums, l, r):
            if l > r:
                return None
            if l == r:
                temp = Node(l, r)
                temp.total = nums[l]
                return temp

            mid = (l + r)//2
            root = Node(l, r)

            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            root.total = root.left.total + root.right.total
            return root
        self.root = createTree(nums, 0,len(nums)-1)

    def update(self, i, val):

        def updateVal(root, i, val):
            if root.start == root.end:
                root.total = val
                return val

            mid = (root.start + root.end) // 2

            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)

            root.total = root.left.total + root.right.total
            return root.total
        return updateVal(self.root, i, val)

    def printTree(self, root):
        if not root:
            return None
        self.printTree(root.left)
        print(root.total)
        self.printTree(root.right)

    def printLevelOrder(self, root):
        if not root:
            return None

        que = deque()
        que.append((root, 0))
        order = defaultdict(list)

        while que:
            t = que.popleft()
            power = t[1]
            order[power].append(t[0].total)

            if t[0].left:
                que.append((t[0].left, power+1))
            if t[0].right:
                que.append((t[0].right, power+1))

        print(order)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    obj = SegmentTree(nums)
    root = obj.root
    # obj.printTree(root)
    obj.printLevelOrder(root)

