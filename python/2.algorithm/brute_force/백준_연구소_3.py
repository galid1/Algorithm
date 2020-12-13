import sys
import copy
from collections import deque


def select_virus(start_idx, cur_viruses):
    global viruses, laboratory, m

    if len(cur_viruses) == m:
        tmp_laboratory, visit = spread_virus(cur_viruses, copy.deepcopy(laboratory))
        update_min_sec(tmp_laboratory, visit, cur_viruses)
        return

    for i in range(start_idx, len(viruses)):
        cur_viruses.append(viruses[i])
        select_virus(i+1, cur_viruses)
        cur_viruses.pop()


def spread_virus(cur_viruses, laboratory):
    global dx, dy, n
    q = deque()
    visit = [[-1 for _ in range(n)] for _ in range(n)]
    for cur_virus in cur_viruses:
        q.append(cur_virus)
        visit[cur_virus[0]][cur_virus[1]] = 0

    # q에서 꺼내어, 조건 확인 후, 시간초 입력
    while q:
        for i in range(len(q)):
            vx, vy = q.popleft()
            for j in range(4):
                next_vx, next_vy = vx + dx[j], vy + dy[j]
                #        연구소 내                                    벽이 아니어야함
                if 0 <= next_vx < n and 0 <= next_vy < n and laboratory[next_vx][next_vy] != 1:
                    # 방문한 적이 없어야함
                    if visit[next_vx][next_vy] < visit[vx][vy]:
                        # 다음 칸이 비활성화 바이러스
                        if laboratory[next_vx][next_vy] == 2 and (next_vx, next_vy) not in cur_viruses:
                            visit[next_vx][next_vy] = visit[vx][vy]
                            q.append((next_vx, next_vy))
                            laboratory[next_vx][next_vy] = 3
                        elif laboratory[next_vx][next_vy] == 0:
                            visit[next_vx][next_vy] = visit[vx][vy] + 1
                            q.append((next_vx, next_vy))
                            laboratory[next_vx][next_vy] = 3

    return laboratory, visit


def update_min_sec(result_laboratory, visit, cur_viruses):
    global min_sec, can_flag

    cur_need_sec = 0
    for i in range(n):
        for j in range(n):
            if result_laboratory[i][j] == 0:
                return
            cur_need_sec = max(cur_need_sec, visit[i][j])

    if cur_viruses == [(1,0), (1,3)]:
        print("===========")
        for v in visit:
            print(v)
    can_flag = True
    min_sec = min(min_sec, cur_need_sec)


min_sec = 51
can_flag = False
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
n, m = map(int, sys.stdin.readline().strip().split(" "))
laboratory = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(n)]
viruses = []
for i in range(n):
    for j in range(n):
        # 바이러스인 경우
        if laboratory[i][j] == 2:
            viruses.append((i, j))

select_virus(0, [])

if not can_flag:
    print(-1)
elif min_sec == 51:
    print(0)
else:
    print(min_sec)