import sys


def do_fall():
    global trees, ds, n

    for i in range(n):
        for j in range(n):
            if not trees[i][j]:
                continue

            for age in trees[i][j]:
                if age % 5 != 0:
                    continue

                for dx, dy in ds:
                    nx, ny = i + dx, j + dy

                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue

                    trees[nx][ny].append(1)


def do_winter():
    global lands, nutrients

    for i in range(n):
        for j in range(n):
            lands[i][j] += nutrients[i][j]


def solve():
    global ds, n, m, k, nutrients, lands, trees

    for year in range(k):

        # 봄, 여름
        for i in range(n):
            for j in range(n):
                if not trees[i][j]:
                    continue
                trees[i][j].sort()
                new_trees = []
                nutrient = 0
                for age in trees[i][j]:
                    if age > lands[i][j]:
                        nutrient += age//2
                    else:
                        lands[i][j] -= age
                        new_trees.append(age+1)
                lands[i][j] += nutrient
                trees[i][j] = new_trees

        # 가을
        do_fall()
        # 겨울
        do_winter()

    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += len(trees[i][j])

    print(cnt)


ds = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
n, m, k = map(int, sys.stdin.readline().strip().split(" "))
lands = [[5 for _ in range(n)] for _ in range(n)]
nutrients = []
for _ in range(n):
    nutrients.append(list(map(int, sys.stdin.readline().strip().split(" "))))
trees = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, age = map(int, sys.stdin.readline().strip().split(" "))
    trees[x-1][y-1].append(age)

solve()