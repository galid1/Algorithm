import sys
from collections import deque


def solve():
    global n, l, w, trucks

    cur_bridge_weight = 0
    bridge = deque([])
    ans = 0

    while trucks:
        # 다리위 아무것도 없는 상태라면 무조건 올리기 가능이므로 여기에 걸리면 bridge가 비지 않은 상태임
        if not can_ride(trucks[0], bridge, cur_bridge_weight):
            out_truck_weight, out_truck_remain_dis = bridge.popleft()
            cur_bridge_weight -= out_truck_weight
            ans += out_truck_remain_dis
            for i in range(len(bridge)):
                bridge[i][1] -= out_truck_remain_dis

            if can_ride(trucks[0], bridge, cur_bridge_weight):
                cur_truck_weight = trucks.popleft()
                bridge.append([cur_truck_weight, l])
                cur_bridge_weight += cur_truck_weight

            continue

        ans += 1
        for i in range(len(bridge)):
            bridge[i][1] -= 1
        if bridge and bridge[0][1] == 0:
            out_truck_weight, out_truck_remain_dis = bridge.popleft()
            cur_bridge_weight -= out_truck_weight
        cur_truck_weight = trucks.popleft()
        bridge.append([cur_truck_weight, l])
        cur_bridge_weight += cur_truck_weight

    if bridge:
        ans += bridge[-1][1]

    print(ans)


def can_ride(cur_truck_weight, bridge, cur_bridge_weight):
    global w, l

    return l > len(bridge) and w >= cur_truck_weight + cur_bridge_weight


n, l, w = map(int, sys.stdin.readline().strip().split(" "))
trucks = deque(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()


# 10 3 9
# 3 4 5 2 4 4 7 1 3 2