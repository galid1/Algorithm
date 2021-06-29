# baekjoon 2805 나무 자르기

import sys

def solution(m, trees):
    trees.sort()

    start_height = 0
    end_height = 2000000000
    mid_height = 0
    cut_len_sum = 0

    while end_height >= start_height :
        mid_height = (end_height + start_height)//2
        cut_len_sum = 0

        #잘라낼때 영향이 미치는 가장 낮은 트리부터 시작하기위해 가장 낮은 인덱스를 찾음
        min_index = 0
        start_idx = 0
        end_idx = len(trees)-1
        while start_idx <= end_idx:
            mid_idx = (start_idx + end_idx)//2

            if trees[mid_idx] == mid_height:
                min_index = mid_idx
                break
            elif trees[mid_idx] > mid_height:
                end_idx = mid_idx - 1
            else:
                start_idx = mid_idx + 1

        # 잘라낸 길이 합 구하기
        for i in range(min_index, len(trees)):
            cut_len = trees[i] - mid_height
            if cut_len > 0:
                cut_len_sum += cut_len

        if cut_len_sum == m:
            print(mid_height)
            return
        elif cut_len_sum > m:
            start_height = mid_height + 1
        else:
            end_height = mid_height - 1

    if cut_len_sum < m:
       mid_height -= 1

    print(mid_height)


n, m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
trees = list(map(int, sys.stdin.readline().rstrip().split(" ")))
solution(m, trees)