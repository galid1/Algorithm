# 효율성 테스트 통과 X
# def solution(info, query):
#     answer = []
#
#     info = list(map(lambda info_line: list(info_line.split(" ")), info))
#     for info_line_idx in range(len(info)):
#         info[info_line_idx][4] = int(info[info_line_idx][4])
#     new_info = sorted(info, key = lambda item: item[4], reverse=True)
#
#     query = list(map(lambda query_line: list(query_line.split("and")), query))
#     new_query = []
#     for query_line in query:
#         new_query_line = list(map(lambda item: item.strip(), query_line))
#         food, grade = new_query_line.pop().split(" ")
#         new_query_line.append(food)
#         new_query_line.append(int(grade))
#         new_query.append(new_query_line)
#
#     for query_line in new_query:
#         cnt = 0
#         for info_line in new_info:
#             if info_line[4] < query_line[4]:
#                 break
#
#             if not predicate(query_line, info_line):
#                 continue
#
#             cnt += 1
#         answer.append(cnt)
#
#     return answer
#
#
# def predicate(query_line, info_line):
#     for idx in range(4):
#         if query_line[idx] == '-':
#             continue
#         if query_line[idx] != info_line[idx]:
#             return False
#
#     return True


def solution(info, query):
    answer = []

    info, query = formatting(info, query)
    indices = make_indices(info)

    for query_line in query:
        answer.append(get_cnt(query_line, indices))

    return answer


def formatting(info, query):
    info = list(map(lambda info_line: info_line.split(' '), info))
    for info_line in info:
        info_line[4] = int(info_line[4])

    query = list(map(lambda query_line: query_line.split('and'), query))
    query = list(map(lambda query_line: list(map(lambda item: item.strip(), query_line)), query))
    for query_line in query:
        food, grade = query_line.pop().split(" ")
        query_line.append(food)
        query_line.append(int(grade))

    return info, query


def make_indices(info):
    indices = {}
    languages = ['-', 'java', 'python', 'cpp']
    positions = ['-', 'backend', 'frontend']
    careers = ['-', 'junior', 'senior']
    foods = ['-', 'chicken', 'pizza']

    for language in languages:
        indices[language] = {}
        for position in positions:
            indices[language][position] = {}
            for career in careers:
                indices[language][position][career] = {}
                for food in foods:
                    indices[language][position][career][food] = []

    for info_line in info:
        insert_info_line(indices, info_line, 0)


    sort_leaf_indices(indices, 0)

    # for k, v in indices.items():
    #     print("key : ", k)
    #     for kk, vv in indices[k].items():
    #         print("sec key : ", kk)
    #         print(vv)
    return indices


def get_cnt(query_line, indices):
    index = indices
    for i in range(4):
        index = index[query_line[i]]

    if not index:
        return 0

    grade = query_line[4]

    left, right = 0, len(index)
    while left < right:  # left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = left + (right - left) // 2

        if index[mid] < grade:
            left = mid + 1
        else:
            right = mid

    return len(index) - right


def insert_info_line(cur_indices, info_line, item_idx):
    if item_idx == 4:
        cur_indices.append(info_line[item_idx])
        return

    insert_info_line(cur_indices[info_line[item_idx]], info_line, item_idx+1)
    insert_info_line(cur_indices['-'], info_line, item_idx + 1)


def sort_leaf_indices(cur_indices, depth):
    if depth == 4:
        cur_indices.sort()
        return

    for k in cur_indices.keys():
        sort_leaf_indices(cur_indices[k], depth+1)


# info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
info = ["java backend junior pizza 103", "java backend junior pizza 102", "java backend junior pizza 101", "java backend junior pizza 102", "java backend junior pizza 102"]
query = ['- and - and - and - 102']
print(solution(info, query))