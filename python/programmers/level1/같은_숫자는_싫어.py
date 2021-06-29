def solution(arr):
    before = arr[0]
    for i in range(1, len(arr)):
        if before == arr[i]:
            arr[i - 1] = -1
        before = arr[i]

    answer = []
    for num in arr:
        if num != -1:
            answer.append(num)

    return answer


print(solution([4,4,4,3,3]))