#hackerranker level order traversal
import queue

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

def levelOrder(root):
    q = queue.Queue()
    q.put(root)
    result = []

    while not q.empty():
        cur = q.get()
        result.append(cur.info)

        if cur.left:
            q.put(cur.left)
        if cur.right:
            q.put(cur.right)
    for i in result:
        print(i,end=' ')

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)