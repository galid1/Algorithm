def solution(record):
    id_nick = {}

    ENTER_CMD = "Enter"
    LEAVE_CMD = "Leave"
    CHANGE_CMD = "Change"

    logs = []
    for row in record:
        row = row.split(" ")
        cmd = row[0]
        id = row[1]

        if cmd == ENTER_CMD:
            id_nick[id] = row[2]
            logs.append([id, "님이 들어왔습니다."])
        elif cmd == LEAVE_CMD:
            logs.append([id, "님이 나갔습니다."])
        elif cmd == CHANGE_CMD:
            id_nick[id] = row[2]

    ans = []
    for id, comment in logs:
        ans.append(id_nick[id] + comment)

    return ans


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)