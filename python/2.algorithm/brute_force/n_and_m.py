# 백준 15649 N과 M

import sys

import sys

def solution(n, m):
    result = []

    for i in range(1, n + 1):
        cur = [str(i)]
        visit = [False for i in range(n + 1)]
        visit[i] = True
        recurisve(i, n, m, cur, visit, result)

    # 결과
    for string in result:
        print(string)


def recurisve(before, n, m, cur, visit, result):
    # 구함
    if len(cur) == m:
        string = ' '.join(cur)
        result.append(string)
        visit[before] = False
        cur.pop()
        return

    # 재귀 호출
    for i in range(1, n + 1):
        if visit[i]:
            continue
        cur.append(str(i))
        visit[i] = True

        recurisve(i, n, m, cur, visit, result)

    # 하나의 for문이 끝났다는 것은 _  _ (_) 가 끝났다는것이므로 (_) 전 자리것을 하나 빼고 다음으로 진행해야됨
    visit[before] = False
    cur.pop()


n, m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
solution(n, m)


# def n_and_m(n, m):
#     digit = 1
#
#     # 1부터 n 까지
#     for i in range(1, n+1):
#         result = []
#         visit = [0 for i in range(m + 1)]
#         visit[digit] = i
#         result.append(i)
#
#         recursive(n, m, digit+1, visit, result)
#
#
# def recursive(n, m, digit, visit, result):
#     if digit > m:
#         for i in result:
#             print(i, end=" ")
#         print()
#         return
#
#     # 1부터 n까지
#     for i in range(1, n+1):
#         if i in visit:
#             continue
#
#         # 방문 처리 및 새로 초기화
#         visit[digit] = i
#         for j in range(digit+1, m+1):
#             visit[j] = 0
#
#         result.append(i)
#         recursive(n, m, digit+1, visit, result)
#
#         result.pop()
#         visit[digit] = 0
#
#
# n, m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
# n_and_m(n, m)
