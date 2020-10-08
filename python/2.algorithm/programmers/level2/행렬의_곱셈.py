def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr2[0]))] for j in range(len(arr1))]

    # arr2의 열만큼 반복
    for a2_col in range(len(arr2[0])):
        # arr1의 행만큼 반복
        for a1_row in range(len(arr1)):
            sums = 0
            # arr1의 행과 arr2의 열을 곱함
            for i in range(len(arr1[0])):
                sums += arr1[a1_row][i] * arr2[i][a2_col]

            answer[a1_row][a2_col] = sums

    return answer


# solution([[1,4], [3,2], [4,1]], [[3,3], [3,3]])
solution([[2,3,2], [4,2,4], [3,1,4]], [[5,4,3], [2,4,1], [3,1,1]])
