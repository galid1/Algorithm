import sys


def solve():
    global n, friends

    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if friends[i][j] == 'N': continue

            visited[i][j] = True
            for k in range(n):
                if friends[j][k] == "N" or k == i: continue

                visited[i][k] = True

    max_cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if visited[i][j]:
                cnt += 1

        max_cnt = max(max_cnt, cnt)

    print(max_cnt)


n = int(sys.stdin.readline().strip())
friends = []

for _ in range(n):
    friends.append(list(sys.stdin.readline().strip()))
solve()


# 10
# NYYYNYYYNY
# YNNNNNNNNY
# YNNYYNNYNY
# YNYNNNNYYY
# NNYNNNYNYN
# YNNNNNYYYY
# YNNNYYNYNN
# YNYYNYYNNN
# NNNYYYNNNY
# YYYYNYNNYN