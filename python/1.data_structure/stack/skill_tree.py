# 프로그래머스 스킬트리 (스택/ 큐)

def solution(skill, skill_trees):
    answer = len(skill_trees)

    for tree in skill_trees:
        temp_skill = list(skill)
        temp_skill.reverse()

        for point in list(tree):
            if point in temp_skill:
                if point != temp_skill.pop():
                    answer -= 1
                    break

    print(answer)

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill, skill_trees)
