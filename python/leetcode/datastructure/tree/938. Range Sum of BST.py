class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.acc = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def in_order(root, low, high):
            if not root:
                return
            in_order(root.left, low, high)
            if low <= root.val <= high:
                self.acc += root.val

            if root.val > high:
                return
            in_order(root.right, low, high)

        in_order(root, low, high)
        return self.acc


n7 = TreeNode(18)
n5 = TreeNode(7)
n4 = TreeNode(3)
n3 = TreeNode(15, None, n7)
n2 = TreeNode(5, n4, n5)
r = TreeNode(10, n2, n3)
low = 7
high = 15

s = Solution()
s.rangeSumBST(r, low, high)
print(s.acc)

