from collections import defaultdict


def solution(id_list, k):
    answer = 0

    id_list = list(map(lambda ids: set(ids.split(" ")), id_list))
    received = defaultdict(int)

    for ids in id_list:
        for id in ids:
            if can_give_to(id, received, k):
                received[id] += 1
                answer += 1

    return answer


def can_give_to(to, received, limit):
    return received[to] < limit


id_list = ["A B C D", "A D", "A B D", "B D"]
k = 2

# id_list = ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"]
# k = 3
print(solution(id_list, k))