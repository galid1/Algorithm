def trap(height):
    l, idx = 0, 1

    answer = 0
    while idx < len(height)-1:
        # 왼쪽 벽 구하기
        while idx < len(height) and height[idx] >= height[l]:
            l = idx
            idx += 1

        # 오른쪽 벽 구하기
        r = idx
        while idx < len(height):
            if height[r] >= height[l]:
                break

            if height[idx] >= height[r]:
                r = idx
            idx += 1

        if r < len(height):
            answer += cal_area(l, r, height)
        l, idx = r, r

    return answer


def cal_area(l, r, height):
    print(l, r)
    h = min(height[l], height[r])
    trap_cnt = r - l + 1 - 2
    total_area = h * trap_cnt

    for i in range(l+1, r):
        total_area -= height[i]

    return total_area

#         0  1  2  3  4  5  6  7  8  9 10  11
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [1,2,3,4,5,4,3,2,1,2,3,2,1,2,3,5]
# height = [4,2,0,3,2,5]
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [5,4,1,2]
height = [1,7,8]
trap(height)