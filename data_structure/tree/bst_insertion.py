#hackerrank binary search tree insertion

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)

        else:
            cur = self.root

            while True:
                if val > cur.info:
                    if not cur.right:
                        cur.right = Node(val)
                        break
                    else:
                        cur = cur.right
                else:
                    if not cur.left:
                        cur.left = Node(val)
                        break
                    else:
                        cur = cur.left



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
