def solution(numbers):
    answer = set()

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            sums = numbers[i] + numbers[j]
            answer.add(sums)

    answer = list(answer)
    answer = sorted(answer)
    return answer


# print(solution([2,1,3,4,1]))
# print(solution([5,0,2,7]))
