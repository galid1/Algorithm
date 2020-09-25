# 1. 빼냄
# 2. 올림 가능 ?
# 3. 올림 (올릴 수 있는 만큼)
# 4.1 올릴 장소가 필요
# 4.2 올릴 장소는 다리 길이만큼 트럭을 소유한뒤 배출
# 4.3 데크에 다리길이와, 무게를 같이 넣는다.
from collections import deque

def solution(bridge_len, bridge_wei, truck_weights):
    answer = 0
    next_truck_index = 0

    bridge = deque()
    cur_bridge_weight = 0

    # 다리위에 트럭이 없고, 트럭이 모두 지나가면 끝내고 time을 return
    while bridge or next_truck_index < len(truck_weights):
        answer += 1
        if bridge:
            # 트럭 위치를 나타내는 짝수자리에 존재하는 값 증가
            for bi in range(0, len(bridge), 2):
                bridge[bi] += 1

            if bridge[0] == bridge_len:
                bridge.popleft()
                cur_bridge_weight -= bridge.popleft()

        # 조건에 맞다면 트럭을 다리 위로
        if next_truck_index < len(truck_weights):
            len_condition = len(bridge)//2 + 1
            # wei_condition = truck_weights[next_truck_index]
            # for bj in range(1, len(bridge), 2):
            #     wei_condition += bridge[bj]

            if len_condition <= bridge_len \
                    and cur_bridge_weight + truck_weights[next_truck_index] <= bridge_wei:
                bridge.append(0)
                bridge.append(truck_weights[next_truck_index])
                cur_bridge_weight += truck_weights[next_truck_index]
                next_truck_index += 1

    print(answer)
    return answer

solution(2, 10, [7,4,5,6])
solution(100, 100, [10])
solution(100, 100, [10,10,10,10,10,10,10,10,10,10])