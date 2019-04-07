#hackerrank Height of binary tree

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def height(root):
    result = []
    stack = []
    root.level = 0
    stack.append(root)

    while len(stack) > 0:
        cur = stack.pop()

        if cur.left:
            cur.left.level = cur.level + 1
            stack.append(cur.left)
        if cur.right:
            cur.right.level = cur.level + 1
            stack.append(cur.right)
        if not cur.left and not cur.right:
            result.append(cur.level)

    return max(result)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))