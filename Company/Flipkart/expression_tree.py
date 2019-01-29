class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data, end="")

def evaluate_expression_tree(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return int(root.data)
    left = evaluate_expression_tree(root.left)
    right = evaluate_expression_tree(root.right)
    if root.data == "*":
        return left * right
    elif root.data == "+":
        return left + right
    elif root.data == "/":
        return left / right
    elif root.data == "-":
        return left - right

if __name__ == "__main__":

    root = TreeNode("+")
    root.left = TreeNode("*")
    root.right = TreeNode("-")
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(100)
    root.right.right = TreeNode("/")
    root.right.right.left = TreeNode(20)
    root.right.right.right = TreeNode(2)

    post_order(root)
    print()
    r = evaluate_expression_tree(root)
    print(r)