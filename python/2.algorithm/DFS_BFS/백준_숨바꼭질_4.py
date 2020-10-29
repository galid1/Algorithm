import sys
from queue import Queue

class Node:
    def __init__(self, value, before):
        self.value = value
        self.before = before


def solution(n, k):
    visit = [0 for i in range(100001)]
    q = Queue()
    visit[n] = 1
    q.put(Node(n, None))
    answer = 0

    while q:
        for i in range(q.qsize()):
            cur = q.get()

            # 정답
            if cur.value == k:
                print(answer)
                arr = [cur.value]
                bef = cur.before
                while True:
                    if not bef:
                        break
                    arr.append(bef.value)
                    bef = bef.before

                for i in range(len(arr)-1, -1, -1):
                    print(arr[i], end=' ')
                return

            for next in (cur.value + 1, cur.value - 1, cur.value * 2):
                if 0 <= next < len(visit) and not visit[next]:
                    visit[next] = 1
                    q.put(Node(next, cur))

        answer += 1


n, k = map(int, sys.stdin.readline().split(" "))
solution(n, k)