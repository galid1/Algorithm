#백준 14226 이모티콘

import sys
import queue

class Node:
    count = 0
    clip = 0
    time = 0
    before = 0

    def __init__(self, count, clip, time, before):
        self.count = count
        self.clip = clip
        self.time = time
        self.before = before

def emoticon(s):
    ELSE = 0
    COPY = 1
    q = queue.Queue()
    visit = [0 for i in range(1001)]

    start = Node(1,0,0,0)
    q.put(start)

    before_clip = -1
    while not q.empty():
        cur = q.get()

        # 정답
        if cur.count == s:
            return cur.time

        # 이미 방문(수가 같으면서 이전클립과 현재 클립이 같으면 이미 방문한것)
        if visit[cur.count] == cur.count and before_clip == cur.clip:
                continue

        # 복사연산 (이전 연산이 복사가 아닌 경우에만)
        if cur.before != COPY:
            q.put(Node(cur.count, cur.count, cur.time + 1, COPY))
        # 붙혀넣기 연산(clip 이 0보다 크고 count+clip가 1000을 넘지 않는 경우에만)
        if cur.clip > 0 and (cur.count+cur.clip) < 1001:
            q.put(Node(cur.count + cur.clip, cur.clip, cur.time + 1, ELSE))
        # 삭제 연산 (삭제시 0보다 큰 경우에만)
        if cur.count - 1 > 0:
            q.put(Node(cur.count - 1, cur.clip, cur.time + 1, ELSE))

        # 방문 처리
        before_clip = cur.clip
        visit[cur.count] = cur.count
        
    return cur.time


s = int(sys.stdin.readline())
print(emoticon(s))