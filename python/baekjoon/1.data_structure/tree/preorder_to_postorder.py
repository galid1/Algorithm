# baekjoon 5639 (이진검색트리 - 전위순회 결과만 주어진것을 이용하여 후위순회 출력)

import sys

class Node:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.value = value
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        new_node = Node(value)

        # root가 None인 경우
        if self.root is None:
            self.root = new_node
            return

        # root가 None이 아닌 경우
        temp = self.root

        while True:
            if value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left

    def post_order(self, root):
        if root.left is not None:
            self.post_order(root.left)
        if root.right is not None:
            self.post_order(root.right)
        print(root.value)


def solution(values):
    b_tree = BinarySearchTree()

    for value in values:
        b_tree.add_node(value)
    b_tree.post_order(b_tree.root)

values = []
while True:
    try:
        values.append(int(input()))
    except:
        break

solution(values)
