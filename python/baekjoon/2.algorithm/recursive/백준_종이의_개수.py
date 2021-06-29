import sys


def solve(si, ei, sj, ej, size):
    global papers, a1, a2, a3

    # 정답
    if size == 1:
        ans_paper = papers[si][sj]
        if ans_paper == -1:
            a1 += 1
        elif ans_paper == 0:
            a2 += 1
        elif ans_paper == 1:
            a3 += 1
        return

    cur_paper = papers[si][sj]
    for i in range(si, ei):
        for j in range(sj, ej):
            if cur_paper != papers[i][j]:
                interval = size // 3
                for k in range(si, ei, interval):
                    for l in range(sj, ej, interval):
                        solve(k, k+interval, l, l+interval, interval)
                return

    if cur_paper == -1:
        a1 += 1
    elif cur_paper == 0:
        a2 += 1
    elif cur_paper == 1:
        a3 += 1


#-1  0  1
a1, a2, a3 = 0, 0, 0
n = int(sys.stdin.readline().strip())
papers = []
for _ in range(n):
    papers.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve(0, n, 0, n, n)

print(a1, a2, a3)