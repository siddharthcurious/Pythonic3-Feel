def printVector(v, i):
    for j in range(i, len(v)):
        print(v[j], end=" ")
    print()

class newNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printKPathUtil(root, path, k):
    if (not root):
        return

    if root.left == None and root.right == None:
        path.append(root.data)
        print(path)

    path.append(root.data)
    printKPathUtil(root.left, path, k)
    printKPathUtil(root.right, path, k)
    path.pop(-1)

def printKPath(root, k):
    path = []
    printKPathUtil(root, path, k)

if __name__ == '__main__':

    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.left.left.left = newNode(6)
    root.left.left.right = newNode(7)
    root.right.right = newNode(8)
    root.right.left = newNode(9)
    root.left.left.left.left = newNode(10)
    root.left.left.left.right = newNode(11)

    k = 12
    printKPath(root, k)

