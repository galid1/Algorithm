class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_length = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root: TreeNode):
            if not root:
                return -1

            l, r = dfs(root.left), dfs(root.right)
            self.max_length = max(self.max_length, l+r+2)

            return max(l, r) + 1

        dfs(root)
        return self.max_length



n4 = TreeNode(4)
n5 = TreeNode(5)
n2 = TreeNode(2)
n3 = TreeNode(3, n4, n5)
r = TreeNode(1, n2, n3)
s = Solution()
print(s.diameterOfBinaryTree(r))