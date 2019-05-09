# 백준 15652 n 과 m 4

import sys

def solution(n, m):
    result = []

    for i in range(n):
        # 1부터
        cur = [i + 1]

        recursive(n, m, cur, result)

    # 결과
    for string in result:
        print(string)


def recursive(n, m, cur, result):
    # 결과 더하기
    if len(cur) == m:
        temp = []
        for j in range(len(cur)):
            temp.append(str(cur[j]))

        result.append(' '.join(temp))
        cur.pop()
        return

    # 재귀 호출
    for i in range(1, n + 1):
        if cur:
            if i < cur[-1]:
                continue
            cur.append(i)
            recursive(n, m, cur, result)

    # 한 반복문이 끝나면 하나를 뽑음
    if cur:
        cur.pop()


n, m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
solution(n, m)