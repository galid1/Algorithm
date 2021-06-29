class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        q = deque()
        q.append(root)

        while q:
            sums = 0
            cnt = 0

            for c in range(len(q)):
                cur = q.popleft()

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

                sums += cur.val
                cnt += 1

            if cnt > 0:
                ans.append(sums / cnt)

        return ans