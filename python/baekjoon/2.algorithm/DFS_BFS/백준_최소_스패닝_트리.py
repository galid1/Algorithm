import sys, heapq

def solve():
    global v, e, g

    visited = [False for _ in range(v+1)]

    res = 0
    selected_cnt = 0
    cur_v = 1
    visited[cur_v] = True
    possible_edges = []
    while True:
        if selected_cnt == v-1:
            return print(res)

        # 현재 정점에서 갈 수 있는 곳을 모두 heap에 넣는다
        for val, to in g[cur_v]:
            if not visited[to]:
                heapq.heappush(possible_edges, (val, to))

        while True:
            val, to = heapq.heappop(possible_edges)
            if not visited[to]:
                break

        selected_cnt += 1
        res += val
        visited[to] = True
        cur_v = to



v, e = map(int, sys.stdin.readline().strip().split(" "))
g = {i:[] for i in range(1, v+1)}

for i in range(e):
    _from, to, val = map(int, sys.stdin.readline().strip().split(" "))
    g[_from].append((val, to))
    g[to].append((val, _from))

solve()

# 7 9
# 1 2 29
# 1 6 10
# 2 3 16
# 2 7 -3
# 3 4 12
# 4 5 22
# 4 7 18
# 5 6 27
# 5 7 -2

# 5 7
# 1 2 1
# 1 4 1
# 1 5 1
# 2 3 5
# 2 4 3
# 3 4 1
# 4 5 4

# 5 7
# 1 2 -7
# 1 4 1
# 1 5 -2
# 2 3 -5
# 2 4 3
# 3 4 1
# 4 5 -4

# 3 3
# 1 2 2
# 1 3 3
# 2 3 9999