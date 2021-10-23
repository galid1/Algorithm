def solution(registered_list, new_id):
    registered = set(registered_list)

    while new_id in registered:
        s, n = split_to_sn(new_id)

        n1 = str(int(n) + 1)
        new_id = s+n1


    answer = new_id
    return answer


def split_to_sn(new_id):
    for idx, c in enumerate(new_id):
        if c.isnumeric():
            return new_id[:idx], new_id[idx:]

    return new_id, "0"


registered_list = ["card", "ace13", "ace16", "banker", "ace17", "ace14"]
new_id = "ace15"
print(solution(registered_list, new_id))
