class TreeNode:
    def __init__(self, name, val=0, left=None, right=None):
        self.name = name
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_lengths = {}

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return -1, -1

            lv, ll = dfs(root.left)
            rv, rl = dfs(root.right)

            # 반환값 구하기
            return_val = root.val
            return_length = 0
            adding_length = 0
            if root.val == lv:
                adding_length = max(adding_length, ll+1)
            if root.val == rv:
                adding_length = max(adding_length, rl+1)
            return_length += adding_length

            # 최대 길이 갱신
            max_length = return_length
            if lv == rv == root.val:
                max_length = max(max_length, ll+rl+2)

            if root.val in self.max_lengths.keys():
                self.max_lengths[root.val] = max(self.max_lengths[root.val], max_length)
            else:
                self.max_lengths[root.val] = max_length

            return return_val, return_length

        dfs(root)
        if not self.max_lengths:
            return 0
        return max(self.max_lengths.items(), key=lambda k: k[1])[1]


# n6 = TreeNode(5)
# n4 = TreeNode(4)
# n5 = TreeNode(4)
# n2 = TreeNode(4, n4, n5)
# n3 = TreeNode(5, None, n6)
# r = TreeNode(1, n2, n3)
# s = Solution()
# print(s.longestUnivaluePath(r))


n7 = TreeNode('n7' , 1)
n8 = TreeNode('n8', 1)
n5 = TreeNode('n5', 1)
n6 = TreeNode('n6', 1)
n4 = TreeNode('n4', 1, n7, n8)
n3 = TreeNode('n3', 1, n5, n6)
n2 = TreeNode('n2', 1, n3, n4)
r = TreeNode('root', 1, None, n2)
s = Solution()
print(s.longestUnivaluePath(r))