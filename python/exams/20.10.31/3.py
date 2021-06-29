from queue import Queue

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(vs):
    answer = []

    # 작물 (0, 1, 2)
    for c in range(3):
        bfs(vs, c, answer)

    return answer

    # 작물


def bfs(vs, c, answer):
    global dx, dy
    cnt = 0
    q = Queue()

    for i in range(len(vs)):
        for j in range(len(vs)):
            if vs[i][j] == c:
                cnt += 1
                q.put([i, j])
                while q.queue:
                    cur = q.get()
                    for k in range(4):
                        nx = cur[0] + dx[k]
                        ny = cur[1] + dy[k]
                        if 0 <= nx < len(vs) and 0 <= ny < len(vs) and vs[nx][ny] == c:
                            vs[nx][ny] = -1
                            q.put([nx, ny])

    answer.append(cnt)



print(solution([[0, 0, 1, 1], [1, 1, 1, 1], [2, 2, 2, 1], [0, 0, 0, 2]]))
