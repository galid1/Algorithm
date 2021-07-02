# # O(N^2)
# def trap(height):
#     l, idx = 0, 1
#
#     answer = 0
#     while idx < len(height)-1:
#         # 왼쪽 벽 구하기
#         while idx < len(height) and height[idx] >= height[l]:
#             l = idx
#             idx += 1
#
#         # 오른쪽 벽 구하기
#         r = idx
#         while idx < len(height):
#             if height[r] >= height[l]:
#                 break
#
#             if height[idx] >= height[r]:
#                 r = idx
#             idx += 1
#
#         if r < len(height):
#             answer += cal_area(l, r, height)
#         l, idx = r, r
#
#     return answer
#
#
# def cal_area(l, r, height):
#     print(l, r)
#     h = min(height[l], height[r])
#     trap_cnt = r - l + 1 - 2
#     total_area = h * trap_cnt
#
#     for i in range(l+1, r):
#         total_area -= height[i]
#
#     return total_area

#==========


def trap(height):
    max_h, max_h_idx = find_max_height(height)

    l_idx, r_idx = 0, len(height) - 1
    max_l_h_idx, max_r_h_idx = l_idx, r_idx

    area = 0
    while l_idx < max_h_idx:
        if l_idx < max_h_idx:
            # 왼쪽 벽중 가장 큰 것이면 갱신
            if height[l_idx] > height[max_l_h_idx]:
                max_l_h_idx = l_idx
            # 왼쪽 벽중 가장 큰것에서 자신의 높이를 뺀 만큼 물이 담김
            area += height[max_l_h_idx] - height[l_idx]
            l_idx += 1

    while r_idx > max_h_idx:
        if r_idx > max_h_idx:
            # 오른쪽 벽 중 가장 큰 것이면 갱신
            if height[r_idx] > height[max_r_h_idx]:
                max_r_h_idx = r_idx
            # 오른쪽 벽중 가장 큰것과 자신의 높이를 뺀 만큼 물이 담김
            area += height[max_r_h_idx] - height[r_idx]
            r_idx -= 1

    return area


def find_max_height(height):
    max_h, max_h_idx = -1, -1

    for idx, h in enumerate(height):
        if h > max_h:
            max_h, max_h_idx = h, idx

    return max_h, max_h_idx

#         0  1  2  3  4  5  6  7  8  9 10  11
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [1,2,3,4,5,4,3,2,1,2,3,2,1,2,3,5]
# height = [4,2,0,3,2,5]
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [5,4,1,2]
height = [1,7,8]
trap(height)