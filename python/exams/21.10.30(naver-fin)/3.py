from collections import defaultdict


class Info:
    def __init__(self):
        self.grades = {}
        self.cnt = 0


def solution(logs):
    answer = []

    dic = init(logs)

    keys = list(dic.keys())

    for idx in range(len(keys)):
        cur_key = keys[idx]
        flag = False
        if cur_key not in dic.keys():
            continue

        for j in range(idx + 1, len(keys)):
            if same(dic[cur_key], dic[keys[j]]):
                answer.append(keys[j])

            if flag:
                answer.append(cur_key)
            del dic[cur_key]

            if not answer:
            return ["None"]
    return answer


def same(one, another):
    return False


def init(logs):
    dic = defaultdict(Info)

    for log in logs:
        stu, prob, grade = log.split(" ")
        prob, grade = int(prob), int(grade)

        info = dic[stu]
        if prob not in info.grades.keys():
            info.grades[prob] = grade
        else:
            info.grades[prob] = max(grade, info.grades[prob])

    return dic


logs = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90",
        "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]
print(solution(logs))
