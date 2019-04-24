# 백준 1026 보물

import sys

def treasure(arr_a, arr_b):
    # 우선 a 배열 정렬
    arr_a.sort()
    new_arr = [0 for i in range(len(arr_a))]
    result = 0


    for i in range(len(arr_a)):
        max_index = -1
        max_num = -1
        for j in range(len(arr_b)):
            if arr_b[j] >= max_num:
                max_num = arr_b[j]
                max_index = j

        result += arr_a[0] * arr_b[max_index]
        arr_a.pop(0)
        arr_b.pop(max_index)

    print(result)

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().rstrip().split(" ")))
b = list(map(int, sys.stdin.readline().rstrip().split(" ")))
treasure(a, b)