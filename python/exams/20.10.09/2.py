from datetime import datetime, timedelta

def solution(n, customers):
    # 손님 시간 변형 (date, 소요 분)
    cus = []
    for c in customers:
        times = c.split(" ")
        mm, dd = map(int, times[0].split("/"))
        h, m, s = map(int, times[1].split(":"))
        spend_m = int(times[2])
        cus.append((datetime(10, mm, dd, h, m, s), spend_m))

    # kisos 매칭수를 세기위한 dict
    cnt = {i:0 for i in range(1, n+1)}

    # 운영중인지 확인을 위한 dict  (0은 운영중이 아님)
    kiosks = {i:0 for i in range(1, n+1)}

    # 매칭
    for tup in cus:
        allocate = False
        # 운영 확인
        for key in kiosks.keys():
            # 할당 가능
            if not kiosks[key]:
                kiosks[key] = tup[0] + timedelta(minutes=tup[1])
                allocate = True
                cnt[key] += 1
                break

        if not allocate:
            min_key = min(kiosks.items(), key=lambda item: item[1] if item[1] else datetime(20, 2, 2, 2, 2, 2))[0]
            kiosks[min_key] = kiosks[min_key] + timedelta(minutes=tup[1])
            cnt[min_key] += 1

    return max(cnt.values(), key=lambda value: value)


print(solution(3, ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]))
print(solution(2, ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"]))