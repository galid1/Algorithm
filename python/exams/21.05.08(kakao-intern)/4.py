from collections import deque


def solution(n, start, end, roads, traps):
    answer = 0

    # 함정지도 만들기
    trap_map = make_trap_map(n, traps)

    # 지도 만들기
    g = make_map(n, roads)
            #         n trap                    bef trap            t                   f
    visited = [[[[False for _ in range(2)] for _ in range(2)] for _ in range(n+1)] for _ in range(n+1)]
    trapped, bef_trapped = 0, 0
    q = deque([(start, answer, trapped, bef_trapped)])

    while q:
        for _ in range(len(q)):
            f, time, trapped, bef_trapped = q.popleft()

            if f == end:
                return time

            # 갈 수 있는곳 탐색
            for t in range(1, n+1):
                # 현재 위치는 넘어가기
                if t == f:
                    continue

                if visited[f][t][bef_trapped][trapped]:
                    continue

                if g[f][0][t] > 0:
                    n_trapped = trapped
                    if trap_map[t]:
                        n_trapped = (n_trapped+1)%2
                        g[t][0], g[t][1] = g[t][1], g[t][0]

                    visited[f][t][trapped][n_trapped] = True
                    q.append((t, time+g[f][0][t], trapped, n_trapped))

    return answer


def make_map(n, roads):
         #정방향, 반대
    g = {i:[[0 for _ in range(n+1)],[0 for _ in range(n+1)]] for i in range(n+1)}
    for p, q, s in roads:
        if g[p][0][q] == 0:
            g[p][0][q] = s
            g[q][1][p] = s
        else:
            g[p][0][q] = min(g[p][0][q], s)
            g[q][1][p] = min(g[q][1][p], s)

    return g


def make_trap_map(n, traps):
    trap_map = [False for _ in range(n+1)]

    for idx in traps:
        trap_map[idx] = True

    return trap_map


# solution(3, 1, 3, [[1,2,2], [3,2,3]], [2])
# solution(4, 1, 4, [[1, 2, 3], [1, 2, 1], [3, 2, 1], [2, 4, 2], [2, 4, 1]], [2,3])
solution(4, 1, 4, [[1, 2, 1], [3, 2, 2], [2, 4, 1]], [2,3])