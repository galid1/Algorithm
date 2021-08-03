class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.acc = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def rec(root):
            if not root:
                return
            self.bstToGst(root.right)
            self.acc += root.val
            root.val = self.acc
            self.bstToGst(root.left)

        rec(root)
        return root


    def in_order(self, root):
        if not root:
            return

        print(root.val)
        self.in_order(root.left)
        self.in_order(root.right)


n7 = TreeNode(7, None, TreeNode(8))
n6 = TreeNode(5)
n5 = TreeNode(2, None, TreeNode(3))
n4 = TreeNode(0)
n3 = TreeNode(6, n6, n7)
n2 = TreeNode(1, n4, n5)
n1 = TreeNode(4, n2, n3)
s = Solution()
s.bstToGst(n1)
s.in_order(n1)