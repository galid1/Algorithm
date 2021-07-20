class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        def make_btree(s, e):
            if s == e:
                return TreeNode(nums[s])

            mid = (s+e)//2
            root = TreeNode(nums[mid])
            if mid - 1 >= s:
                root.left = make_btree(s, mid-1)
            if mid + 1 <= e:
                root.right = make_btree(mid+1, e)

            return root

        nums.sort()
        root = make_btree(0, len(nums)-1)
        self.pre(root)
        return root

    def in_order(self, root):
        if not root:
            return

        print(root.val)
        self.in_order(root.left)
        self.in_order(root.right)


nums = [-10, -7, 1, 5, -1, 0, 10, 7, -5]

s = Solution()
s.sortedArrayToBST(nums)
