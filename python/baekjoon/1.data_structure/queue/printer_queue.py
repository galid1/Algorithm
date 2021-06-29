# baekjoon 1966 프린터 큐

import sys
import collections

def solution(docs, n):
    result = 1
    print_index = n

    # print_index가 출력될때 break
    while True:
        bigger_index = -1
        max_num = docs[0]
        # 현재 큐 제일앞보다 큰 수가 있는지 찾는다(가장 큰 수)
        for i in range(1, len(docs)):
            if max_num < docs[i]:
                bigger_index = i
                max_num = docs[i]

        # 더 큰 수가 있는 경우
        if bigger_index > -1:
            for j in range(bigger_index):
                if print_index == 0:
                    print_index = len(docs) - 1
                else:
                    print_index -= 1
                docs.append(docs.popleft())

        # 지금 큐에서 제거하는 인덱스가 찾는 인덱스 인 경우
        if print_index == 0:
            print(result)
            return
        # 아니라면 제잎 앞의 수를 제거하고 print index를 한칸 당김
        docs.popleft()
        print_index -= 1
        result += 1

t = int(sys.stdin.readline())
for i in range(t):
    m, n = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    docs = collections.deque(list(map(int, sys.stdin.readline().rstrip().split(" "))))
    solution(docs, n)