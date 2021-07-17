class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# dfs 재귀로 풀이
# class Solution:
#     def __init__(self):
#         self.max_depth = 0
#
#     def maxDepth(self, root) -> int:
#         def dfs(depth, parent):
#             if not parent.left and not parent.right:
#                 self.max_depth = max(self.max_depth, depth)
#
#             if parent.left:
#                 dfs(depth + 1, parent.left)
#             if parent.right:
#                 dfs(depth + 1, parent.right)
#
#         if not root:
#             return 0
#         dfs(1, root)
#         return self.max_depth

# bfs로 풀이
from collections import deque

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        q = deque()
        q.append(root)

        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                cur_node = q.popleft()
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

        return depth

n4 = TreeNode(4)
n5 = TreeNode(5)
n2 = TreeNode(2)
n3 = TreeNode(3, n4, n5)
r = TreeNode(1, n2, n3)
s = Solution()
print(s.maxDepth(r))

