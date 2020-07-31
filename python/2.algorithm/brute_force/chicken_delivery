# 백준 15686 치킨 배달

import sys

# n, m, chicken_map 입력받기
n, m = map(int, sys.stdin.readline().split(" "))
f = []

for i in range(n):
    f.append(list(map(int, sys.stdin.readline().strip().split(" "))))

chicken_list = []
home_list = []
chicken_load_list = []


# 치킨집과 집을 chicken_map으로부터 찾아서 list에 저장
def find_chicken_and_home():
    global f, chicken_list, home_list

    for row in range(len(f)):
        for col in range(len(f[0])):
            if f[row][col] == 1:
                home_list.append([row, col])
            if f[row][col] == 2:
                chicken_list.append([row, col])


def choice_do_not_destroy_chicken(visit_list, choose_chicken_list, i, remain_choice_count):
    if remain_choice_count <= 0:
        cal_chicken_load(choose_chicken_list)
        return

    for j in range(i, len(chicken_list)):
        if j not in choose_chicken_list:
            visit_list.append(j)
            choose_chicken_list.append(j)
            choice_do_not_destroy_chicken(visit_list, choose_chicken_list, j+1, remain_choice_count - 1)
            visit_list.pop()
            choose_chicken_list.pop()


def cal_chicken_load(choose_chicken_list):
    global chicken_list, home_list, chicken_load_list
    sum_of_chicken_load = 0

    for home in home_list:
        min_chicken_load = 30000
        for choose_chicken_index in choose_chicken_list:
            chicken_load = abs(abs(home[0] - chicken_list[choose_chicken_index][0]) + abs(home[1] - chicken_list[choose_chicken_index][1]))
            min_chicken_load = min(min_chicken_load, chicken_load)

        sum_of_chicken_load = sum_of_chicken_load + min_chicken_load

    chicken_load_list.append(sum_of_chicken_load)


find_chicken_and_home()
choice_do_not_destroy_chicken([], [], 0, m)
print(min(chicken_load_list))