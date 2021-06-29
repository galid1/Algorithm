import sys, copy


def get_fish_idx(x, y, fish_list):
    for idx, fish in enumerate(fish_list):
        if fish[2][0] == x and fish[2][1] == y:
            return idx
    # 해당 좌표의 물고기가 없는 경우
    return -1


def is_valid(x, y):
    return 0 <= x < 4 and 0 <= y < 4


def move_fishes(sx, sy, fish_list):
    global ds

    for idx, fish in enumerate(fish_list):
        cur_d = fish[1]
        cx, cy = fish[2]
        for _ in range(8):
            nx, ny = cx+ds[cur_d][0], cy + ds[cur_d][1]
            # 이동 가능
            if (nx != sx or ny != sy) and is_valid(nx, ny):
                will_fish_idx = get_fish_idx(nx, ny, fish_list)
                # 이동하려는 칸에 물고기 존재
                if will_fish_idx != -1:
                    fish_list[will_fish_idx][2] = [cx, cy]
                fish_list[idx][1] = cur_d
                fish_list[idx][2] = [nx, ny]
                break

            cur_d = (cur_d + 1) % 8


def solve(sx, sy, sd, eat_fish_sum, fish_list):
    global ds, ans

    move_fishes(sx, sy, fish_list)

    cx, cy = sx, sy
    while True:
        nsx, nsy = cx+ds[sd][0], cy+ds[sd][1]

        # 더이상 이동 불가
        if not is_valid(nsx, nsy) or not fish_list:
            ans = max(ans, eat_fish_sum)
            return

        will_eat_fish_idx = get_fish_idx(nsx, nsy, fish_list)

        # 이동하려는 칸에 물고기 존재
        if will_eat_fish_idx != -1:
            will_eat_fish_num = fish_list[will_eat_fish_idx][0]
            will_eat_fish_dir = fish_list[will_eat_fish_idx][1]
            n_fish_list = copy.deepcopy(fish_list)
            del n_fish_list[will_eat_fish_idx]
            solve(nsx, nsy, will_eat_fish_dir, eat_fish_sum + will_eat_fish_num, n_fish_list)

        cx, cy = nsx, nsy


# 입력
ds = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
fishes = []
for i in range(4):
    infos = list(map(int, sys.stdin.readline().strip().split(" ")))

    for j in range(0, 8, 2):
        #                    번호,       방향           위치
        fishes.append([infos[j], infos[j + 1] - 1, [i, j // 2]])
fishes.sort(key=lambda fish: fish[0])

zero_zero_fish_idx = get_fish_idx(0, 0, fishes)
eat_fish_sum = fishes[zero_zero_fish_idx][0]
sd = fishes[zero_zero_fish_idx][1]
del fishes[zero_zero_fish_idx]

ans = eat_fish_sum
solve(0, 0, sd, eat_fish_sum, fishes)
print(ans)
