import sys, heapq


def solve():
    global n, m, x, maps

    #
    to_x_min_dist = [sys.maxsize for i in range(n+1)]

    for i in range(1, n+1):
        if i == x:
            continue

        cur_i_min_dist = dijkstra(i)
        to_x_min_dist[i] = cur_i_min_dist[x]

    ans = 0
    from_x_min_dist = dijkstra(x)
    for i in range(1, n+1):
        if i == x:
            continue

        ans = max(ans, from_x_min_dist[i] + to_x_min_dist[i])

    print(ans)


def dijkstra(start):
    global n, maps
    INF = sys.maxsize

    results = [INF if start != i else 0 for i in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    visited[start] = True

    hq = []

    for v, w in maps[start].items():
        heapq.heappush(hq, (w, v))

    while hq:
        cur_w, cur_v = heapq.heappop(hq)

        if visited[cur_v]:
            continue

        visited[cur_v] = True
        results[cur_v] = cur_w

        for cur_v_linked_v, cur_v_edge_weight in maps[cur_v].items():
            if visited[cur_v_linked_v]:
                continue

            heapq.heappush(hq, (results[cur_v] + cur_v_edge_weight, cur_v_linked_v))

    return results


n, m, x = map(int, sys.stdin.readline().strip().split(' '))

maps = {i: {} for i in range(1, n+1)}
for _ in range(m):
    f, t, c = map(int, sys.stdin.readline().strip().split(" "))
    maps[f][t] = c

solve()