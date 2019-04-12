# 백준 13549 숨바꼭질3

# *2가 0이라는것은 계속해서 *2를 할 수도 있음을 알아야함
# queue를 바꾸는 아이디어는 제일 아래 방법이 더나은듯

import sys
import queue

class Node:
    def __init__(self, value, time):
        self.value = value
        self.time = time

def hide_and_seek_3(n, k):
    visit = [0 for i in range(100001)]
    q = []
    q.append(queue.Queue())
    q.append(queue.Queue())
    a,b = 1,0

    q[0].put(Node(n, 0))

    while True:
        # queue 바꾸기
        a,b = b,a
        # 순간이동 처리
        for i in range(len(q[a].queue)):
            teleport = q[a].queue[i].value * 2

            # 순간이동 최대치 까지 함 (단 0인 경우제외)
            if teleport > 0 :
                while teleport <= 100000:
                    if visit[teleport] == 0:
                        q[a].put(Node(teleport, q[a].queue[i].time))
                        visit[teleport] = 1
                    teleport *= 2

        # 다음 노드 처리
        while not q[a].empty():
            cur = q[a].get()
            # 찾음(정답)
            if cur.value == k:
                print(cur.time)
                return

            if cur.value + 1 <= 100000:
                if visit[cur.value + 1] == 0:
                    q[b].put(Node(cur.value + 1, cur.time + 1))
                    visit[cur.value + 1] = 1
            if cur.value - 1 >= 0:
                if visit[cur.value - 1] == 0:
                    q[b].put(Node(cur.value - 1, cur.time + 1))
                    visit[cur.value - 1] = 1


n,k = list(map(int, sys.stdin.readline().rstrip().split(" ")))
hide_and_seek_3(n, k)


# def hide_and_seek_3(n, k):
#     visit = [0 for i in range(100001)]
#     now_queue = queue.Queue()
#     next_queue = queue.Queue()
#
#     now_queue.put(Node(n, 0))
#     visit[n] = 1
#
#     while not now_queue.empty():
#         cur = now_queue.get()
#
#         # 정답
#         if cur.value == k:
#             print(cur.time)
#             return
#
#         # 순간이동 처리
#         if cur.value > 0:
#             teleport = cur.value * 2
#             while teleport <= 100000:
#                 if visit[teleport] != 1:
#                     now_queue.put(Node(teleport, cur.time))
#                     visit[teleport] = 1
#                 teleport *= 2
#
#         # + 1 처리
#         if cur.value + 1 <= 100000:
#             if visit[cur.value + 1] != 1:
#                 next_queue.put(Node(cur.value + 1, cur.time + 1))
#                 visit[cur.value + 1] = 1
#
#         # - 1 처리
#         if cur.value - 1 >= 0:
#             if visit[cur.value - 1] != 1:
#                 next_queue.put(Node(cur.value - 1, cur.time + 1))
#                 visit[cur.value - 1] = 1
#
#         if now_queue.empty():
#             now_queue = next_queue
#             next_queue = queue.Queue()