import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    min_diff = sys.maxsize
    bef = -1

    def minDiffInBST(self, root: TreeNode) -> int:
        def in_order(root):
            if root.left:
                in_order(root.left)

            if self.bef != -1:
                self.min_diff = min(self.min_diff, abs(root.val - self.bef))
            self.bef = root.val

            if root.right:
                in_order(root.right)

        in_order(root)
        return self.min_diff


n5 = TreeNode(3)
n4 = TreeNode(1)
n3 = TreeNode(6)
n2 = TreeNode(2, n4, n5)
r = TreeNode(4, n2, n3)

s = Solution()
s.minDiffInBST(r)