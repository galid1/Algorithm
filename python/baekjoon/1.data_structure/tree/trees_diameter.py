# baekjoon 1167 트리의 지름

# baekjoon 1167 트리의 지름

import sys


class Node:
    def __init__(self, num, infos, cur_distance = 0):
        self.num = num
        self.links_info = []
        self.cur_distance = cur_distance

class Node_Info:
    def __init__(self, num, distance):
        self.num = num
        self.distance = distance

# 트리 생성
def create_tree(infos):
    # 노드들이 순차적으로 담김 1.2.3.4.5...
    tree = [Node(i, infos) for i in range(len(infos) + 1)]

    for info in infos:
        # 노드 정보에 담긴 노드의 번호를 이용해 tree배열에서 노드를 가져옴
        cur_node = tree[info[0]]

        # 정점 번호, 마지막 정보인 -1 을 제외하고 for
        for i in range(1, len(info) - 1, 2):
            node_info = Node_Info(info[i], info[i+1])
            cur_node.links_info.append(node_info)

    return tree


def clear_tree(tree):
    for node in tree:
        node.cur_distance = 0


def find_longest_distance(tree, start_node):
    # 방문배열(1,2,3,4,5로 하기 위해 tree의 길이로함)
    visit = [False for i in range(len(tree))]

    # 스택 생성 및 시작정점 삽입
    stack = []
    stack.append(tree[start_node])

    diameter_node = tree[start_node]

    # 스택이 빌때 까지
    while stack:
        cur = stack.pop()
        visit[cur.num] = True

        # 더 방문할 것이 있는지 파악, 즉 막다른 노드인지 여부
        any_visit = False

        # 현재 노드의 연결정보를 가져옴
        for link_node_info in cur.links_info:
            # 방문한적이 없는 경우
            if not visit[link_node_info.num]:
                link_node = tree[link_node_info.num]
                link_node.cur_distance = cur.cur_distance + link_node_info.distance
                stack.append(link_node)
                any_visit = True

        # 막다른 노드임
        if not any_visit and cur.cur_distance > diameter_node.cur_distance:
            diameter_node = cur

    return diameter_node


def solution(infos):
    tree = create_tree(infos)

    diameter_node_1 = find_longest_distance(tree, 1)
    clear_tree(tree)
    diameter = find_longest_distance(tree, diameter_node_1.num)

    print(diameter.cur_distance)


v = int(sys.stdin.readline())
v_infos = []
for i in range(v):
    v_infos.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))
solution(v_infos)
