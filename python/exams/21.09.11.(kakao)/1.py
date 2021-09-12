from collections import defaultdict

def solution(id_list, report, k):
    reported_cnt = defaultdict(set)

    for report, reported in list(map(lambda item: item.split(" "), report)):
        reported_cnt[reported].add(report)

    mail_cnt = {user_id:0 for user_id in id_list}

    for reported, report_set in reported_cnt.items():
        if len(report_set) >= k:
            for report in report_set:
                mail_cnt[report] += 1

    return list(mail_cnt.values())


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))