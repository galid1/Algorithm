class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root) -> int:
        def dfs(depth, parent):
            if not parent.left and not parent.right:
                self.max_depth = max(self.max_depth, depth)

            if parent.left:
                dfs(depth + 1, parent.left)
            if parent.right:
                dfs(depth + 1, parent.right)

        if not root:
            return 0
        dfs(1, root)
        return self.max_depth


n4 = TreeNode(4)
n5 = TreeNode(5)
n2 = TreeNode(2)
n3 = TreeNode(3, n4, n5)
r = TreeNode(1, n2, n3)
s = Solution()
print(s.maxDepth(r))

