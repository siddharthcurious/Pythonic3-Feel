from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    q = deque()
    q.append(root)

    while q:
        temp = q.popleft()
        if temp.left:
            q.append(temp.left)
        else:
            temp.left = TreeNode(data)
            return

        if temp.right:
            q.append(temp.right)
        else:
            temp.right = TreeNode(data)
            return


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

if __name__ == "__main__":

    root = TreeNode(10)
    insert(root, 17)
    insert(root, 11)
    insert(root, 12)
    insert(root, 15)
    inorder(root)