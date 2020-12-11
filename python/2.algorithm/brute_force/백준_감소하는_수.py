import sys


def dfs(cur_num, limit):
    global answer, idx, n, answers

    # 재귀 종료
    if len(cur_num) == limit:
        idx += 1
        answers.append(cur_num)
        # 정답이 존재
        if idx == n:
            print(cur_num)
            sys.exit()
        return

    if not cur_num:
        for i in range(10):
            dfs(str(i), limit)
    else:
        for j in range(int(cur_num[-1])):
            dfs(cur_num + str(j), limit)


answer, idx = 0, -1
answers = []
n = int(sys.stdin.readline())
for i in range(1, 11):
    dfs('', i)
print(-1)