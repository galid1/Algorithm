def solution(arr):
    answer = []

    min_num = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if min_num > arr[i]:
            min_index = i
            min_num = arr[i]

    for j in range(len(arr)):
        if j == min_index:
            continue
        answer.append(arr[j])

    if len(answer) == 0:
        return [-1]

    return answer

print(solution([4,3,2,1]))
print(solution([10]))
print(solution([5,1,2,3,7,6,8,9]))