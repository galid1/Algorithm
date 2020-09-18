def solution(participants, completions):
    answer = ''

    participant_count = {}

    # 참여자 명단 초기화
    for participant in participants:
        participant_count[participant] = 0

    # 이름에 해당하는 참여자수 기록
    for participant in participants:
        participant_count[participant] += 1

    # 완료한 선수만큼 참여자수 차감
    for completion in completions:
        participant_count[completion] -= 1

    for key in participant_count.keys():
        if participant_count[key] > 0:
            answer = key
            break

    return answer


from collections import Counter

#
# def solution(participants, completions):
#     answer = Counter(participants) - Counter(completions)
#     return list(answer.keys())[0]
#
# print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))

