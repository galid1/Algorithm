# baekjoon 2493 탑

import sys
import collections

# class Tower:
#     def __init__(self, height, index):
#         self.height = height
#         self.index = index
#
# def tower(towers):
#     # 결과 (첫 타워는 무조건 0)
#     result = [0]
#     # 현재 타워 목록
#     cur_towers = collections.deque()
#     # 시작타워 삽입
#     cur_towers.append(Tower(towers.popleft(), 1))
#
#     # 입력된 타워들을 모두 순회
#     for i in range(2, len(towers)+2):
#         cur_tower = Tower(towers.popleft(), i)
#
#         flag = False
#         for j in range(len(cur_towers)):
#             standing_tower = cur_towers.pop()
#
#             # 제일 오른쪽에 서있는 타워가 지금 꺼낸 타워보다 작은 경우 다음 서 있는 타워로 진행
#             if cur_tower.height > standing_tower.height:
#                 continue
#
#             # 만약 서있는 타워가 지금 타워보다 높다면
#             result.append(standing_tower.index)
#             cur_towers.append(standing_tower)
#             cur_towers.append(cur_tower)
#             flag = True
#             break
#
#         if not flag:
#             result.append(0)
#             cur_towers.append(cur_tower)
#
#     for value in result:
#         print(value, end=" ")
#
# n = int(sys.stdin.readline())
# towers = collections.deque(list(map(int, sys.stdin.readline().rstrip().split(" "))))
# tower(towers)

class Tower:
    def __init__(self, height, index):
        self.height = height
        self.index = index

def solution(heights):
    answer = [0]
    stack = [Tower(heights[0],1)]

    for i in range(1, len(heights)):
        cur_tower = Tower(heights[i], i+1)
        change = False
        for j in range(len(stack) - 1, -1, -1):
            if stack[j].height <= heights[i] :
                stack.pop()
            else:
                answer.append(stack[j].index)
                stack.append(cur_tower)
                change = True
                break
        if not change:
            answer.append(0)
            stack.append(cur_tower)

    print(answer)

    return answer

# heights = [6, 9, 5, 7, 4]
heights = [3, 9, 9, 3, 5, 7, 2]
solution(heights)