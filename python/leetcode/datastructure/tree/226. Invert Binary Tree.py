class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return

            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root

    # def inorder(self, root):
    #     if not root:
    #         return
    #
    #     print(root.val)
    #     self.inorder(root.left)
    #     self.inorder(root.right)


n7 = TreeNode(9)
n6 = TreeNode(6)
n5 = TreeNode(3)
n4 = TreeNode(1)
n3 = TreeNode(7, n6, n7)
n2 = TreeNode(2, n4, n5)
r = TreeNode(4, n2, n3)
s = Solution()
print(s.invertTree(r))