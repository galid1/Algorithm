import sys


def solve():
    global n

    if n < 10:
        return print(n)

    n -= 9

    for r in range(2, 11):
        for i in range(1, 10):
            dfs(r-1, [i])

            if n <= 0:
                return

    if n > 0:
        print(-1)


def dfs(r, cur):
    global n

    if r == 0:
        n -= 1
        if n == 0:
            print(''.join(list(map(str, cur))))
        return

    for i in range(10):
        if cur[-1] <= i:
            return

        cur.append(i)
        dfs(r-1, cur)
        cur.pop()


n = int(sys.stdin.readline().strip())
solve()


# import sys
#
#
# def dfs(cur_num, limit):
#     global answer, idx, n, answers
#
#     # 재귀 종료
#     if len(cur_num) == limit:
#         idx += 1
#         answers.append(cur_num)
#         # 정답이 존재
#         if idx == n:
#             print(cur_num)
#             sys.exit()
#         return
#
#     if not cur_num:
#         for i in range(10):
#             dfs(str(i), limit)
#     else:
#         for j in range(int(cur_num[-1])):
#             dfs(cur_num + str(j), limit)
#
#
# answer, idx = 0, -1
# answers = []
# n = int(sys.stdin.readline())
# for i in range(1, 11):
#     dfs('', i)
# print(-1)