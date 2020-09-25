def solution(prerequisite, user_skills):
    answer = 0

    for user_skill in user_skills:
        prerequisite_idx = 0

        for user_skill_i in range(len(user_skill)):
            cur_skill = user_skill[user_skill_i]

            if cur_skill not in prerequisite:
                continue

            if prerequisite[prerequisite_idx] != cur_skill:
                break
            else:
                prerequisite_idx += 1
        else:
            answer += 1

    return answer


solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"])

