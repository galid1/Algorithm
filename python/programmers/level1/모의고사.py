def solution(answers):
    answer = []

    first_man = [1,2,3,4,5]
    second_man = [2,1,2,3,2,4,2,5]
    third_man = [3,3,1,1,2,2,4,4,5,5]

    first_count = cal_answer(first_man, answers)
    second_count = cal_answer(second_man, answers)
    third_count = cal_answer(third_man, answers)

    max_count = max(first_count, second_count, third_count)
    if first_count >= max_count:
        answer.append(1)
    if second_count >= max_count:
        answer.append(2)
    if third_count >= max_count:
        answer.append(3)

    return answer


def cal_answer(pattern, answers):
    correct_count = 0

    for i in range(len(answers)):
        correct_answer = answers[i]
        answer = pattern[i%len(pattern)]
        if correct_answer == answer:
            correct_count += 1

    return correct_count


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))