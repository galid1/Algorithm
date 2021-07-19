class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.is_balanced = True

    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not self.is_balanced:
                return -1

            if not root:
                return -1

            lh = dfs(root.left)
            rh = dfs(root.right)

            if abs(lh - rh) > 1:
                self.is_balanced = False

            return max(lh, rh) + 1

        dfs(root)
        return self.is_balanced



# n3 = TreeNode(3)
# n2 = TreeNode(2)
# n1 = TreeNode(1, n2, n3)
# [1,2,3,4,5,6,null,8]


n8 = TreeNode(8)
n7 = TreeNode(7)
n6 = TreeNode(6)
n5 = TreeNode(5)
n4 = TreeNode(4, n8)
n3 = TreeNode(3, n6, None)
n2 = TreeNode(2, n4, n5)
n1 = TreeNode(1, n2, n3)

s = Solution()
print(s.isBalanced(n1))