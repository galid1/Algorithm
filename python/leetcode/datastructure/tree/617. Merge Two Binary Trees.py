class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        elif root1:
            node = TreeNode(root1.val)
            node.left = self.mergeTrees(root1.left, None)
            node.right = self.mergeTrees(root1.right, None)
            return node
        elif root2:
            node = TreeNode(root2.val)
            node.left = self.mergeTrees(None, root2.left)
            node.right = self.mergeTrees(None, root2.right)
            return node


n7 = TreeNode(9)
n6 = TreeNode(6)
n5 = TreeNode(3)
n4 = TreeNode(1)
n3 = TreeNode(7, n6, n7)
n2 = TreeNode(2, n4, n5)
r = TreeNode(4, n2, n3)
s = Solution()
print(s.mergeTrees(r))

