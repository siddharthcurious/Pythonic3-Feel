# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root, prev, cnt, max_cnt, result):
            if not root:
                return prev, cnt, max_cnt

            prev, cnt, max_cnt = inorder(root.left, prev, cnt, max_cnt, result)
            if prev:
                if root.val == prev.val:
                    cnt += 1
                else:
                    cnt = 1
            if cnt > max_cnt:
                max_cnt = cnt
                del result[:]
                result.append(root.val)
            elif cnt == max_cnt:
                result.append(root.val)
            return inorder(root.right, root, cnt, max_cnt, result)

        if not root:
            return []
        result = []
        inorder(root, None, 1, 0, result)
        return result

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root, prev, cnt, max_cnt, results):
            if not root:
                return prev, cnt, max_cnt

            prev, cnt, max_cnt = inorder(root.left, prev, cnt, max_cnt, results)
            if prev:
                if prev.val == root.val:
                    cnt += 1
                else:
                    cnt = 1

            if cnt > max_cnt:
                max_cnt = cnt
                del results[:]
                results.append(root.val)
            elif cnt == max_cnt:
                results.append(root.val)

            return inorder(root.right, root, cnt, max_cnt, results)

        if not root:
            return []

        results = []
        inorder(root, None, 1, 0, results)
        return results

if __name__ == "__main__":

    s = Solution()

    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.right.right = TreeNode(4)

    r = s.findMode(root)
    print(r)


