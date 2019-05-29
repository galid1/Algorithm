# 백준 2250 트리의 높이와 너비

import sys, collections

class Node:
    def __init__(self, num, parent=None, left = None, right = None):
        self.num = num
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0
        self.width = 0


def in_order(tree, tree_level, root, h, w):
    temp_w = w

    #좌측
    if root.left is not None :
        temp_w = in_order(tree, tree_level, root.left, h+1, w)
        temp_w += 1

    tree[root.num].height = h
    tree[root.num].width = temp_w
    # 레벨별 트리에 저장
    n = Node(root.num)
    n.height = h
    n.width = temp_w

    tree_level[h].append(n)

    #우측
    if root.right is not None :
        temp_w = in_order(tree, tree_level, root.right, h+1, temp_w + 1)

    return temp_w


def find_length(tree_width_info):
    if tree_width_info:
        start_node = tree_width_info.popleft()
        end_node = None

        for node in tree_width_info:
            if end_node is None:
                end_node = node
                continue

            if node.width > end_node.width:
                end_node = node

        if end_node is None:
            return 1

        return end_node.width - start_node.width + 1


# 임의의 정점으로부터 계속해서 부모를찾음 None이면 그것이 루트
def find_root(node):
    temp = node
    while temp.parent is not None:
        temp = temp.parent
    return temp


def solution(infos):
    result_num = 1
    result_width = 0

    # 트리 생성
    tree = [Node(i) for i in range(0, len(infos)+1)]
    # 레벨별 트리가 저장될 배열
    tree_level_info = [[] for i in range(10001)]

    for info in infos:
        cur_node = tree[info[0]]
        if info[1] != -1:
            cur_node.left = tree[info[1]]
            cur_node.left.parent = cur_node
        if info[2] != -1:
            cur_node.right = tree[info[2]]
            cur_node.right.parent = cur_node

    # 트리의 루트 찾기
    root_node = find_root(tree[1])

    # 중위 순회를 통해 높이와 너비 정하기
    in_order(tree, tree_level_info, tree[root_node.num], 1, 1)

    # 가장 긴 너비와 그 번호 구하기 , 높이 0 제외 1부터
    index = 1
    while len(tree_level_info[index]) > 0 :
        temp_width = find_length(collections.deque(tree_level_info[index]))

        if temp_width is not None:
            if temp_width > result_width:
                result_width = temp_width
                result_num = index

        index += 1

    print(result_num, result_width)



n = int(sys.stdin.readline())
tree_infos = []
for i in range(n):
    tree_infos.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

solution(tree_infos)