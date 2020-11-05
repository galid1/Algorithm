import sys


def solution(row):         #우하 #좌하
    global n, answer, cols, lrds, rlds

    # 정답
    if row == n:
        answer += 1
        return

    for i in range(n):
        lrd = row - i + n - 1
        rld = row + i
        if i not in cols and lrd not in lrds and rld not in rlds:
            cols.append(i)
            lrds.append(lrd)
            rlds.append(rld)
            solution(row + 1)
            cols.pop()
            lrds.pop()
            rlds.pop()


n = int(sys.stdin.readline())
answer = 0
cols = []
lrds = []
rlds = []
solution(0)
print(answer)