class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.p_idx = 0
        self.i_idx = 0

    def buildTree(self, preorder, inorder) -> TreeNode:
        def recur(root):
            p_val = preorder[self.p_idx]
            i_val = inorder[self.i_idx]

            if p_val == i_val:
                root.left = TreeNode(p_val)
                self.p_idx += 1
                self.i_idx += 1
            if root.left:
                recur(root.left)





        root = TreeNode(preorder[self.p_idx])
        self.p_idx += 1
        recur(root)
        return root


class Test:
    def in_o(self,root):
        if not root:
            return

        self.in_o(root.left)
        print(root.val)
        self.in_o(root.right)


    def p_o(self, root):
        if not root:
            return

        print(root.val)
        self.p_o(root.left)
        self.p_o(root.right)



n5 = TreeNode(7)
n4 = TreeNode(2)
n3 = TreeNode(4, n4)
n2 = TreeNode(5, n5)
n1 = TreeNode(1, None, n3)
r = TreeNode(3, n1, n2)
t = Test()

# 중위
t.in_o(r)
