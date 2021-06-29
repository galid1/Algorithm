def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr1[0]))] for j in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] += arr1[i][j]

    for i in range(len(arr2)):
        for j in range(len(arr2[0])):
            answer[i][j] += arr2[i][j]
    return answer

# solution([[1,2], [2,3]], [[3,4], [5,6]])
# solution([[1],[2]], [[3],[4]])
#
#
# n = [[1, 2], [3, 4], [5, 6]]
#
# answer = [0 for i in range(len(n[0]))]
#
# for i in range(len(n)):
#     for j in range(len(n[0])):
#         answer[j] += n[i][j]
#
# print(answer)