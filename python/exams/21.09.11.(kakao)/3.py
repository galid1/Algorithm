from datetime import datetime
import math


def solution(fees, records):
    answer = []

    acc_times = record_parking_time(records)
    acc_times = list(sorted(acc_times.items(), key=lambda item: item[0]))

    for num, parking_time in acc_times:
        answer.append(cal_fee(fees, parking_time))

    return answer


def record_parking_time(records):
    acc_times = {}
    park_status = {}

    for out_time, num, type in list(map(lambda record: record.split(" "), records)):
        if type == "IN":
            park_status[num] = out_time
        else:
            entry_time = park_status.pop(num)
            parking_time = cal_parking_time(entry_time, out_time)

            if num not in acc_times.keys():
                acc_times[num] = parking_time
            else:
                acc_times[num] += parking_time

    # 출차 기록이 없는 차들의 주차 시간 계산
    for num, entry_time in park_status.items():
        parking_time = cal_parking_time(entry_time, "23:59")

        if num not in acc_times.keys():
            acc_times[num] = parking_time
        else:
            acc_times[num] += parking_time

    return acc_times


def cal_parking_time(entry_time, out_time):
    format_str = "%H:%M"
    diff = datetime.strptime(out_time, format_str) - datetime.strptime(entry_time, format_str)
    diff_min = int(diff.total_seconds()//60)
    return diff_min


def cal_fee(fee_table, parking_time_min):
    basic_time, basic_fee, unit_time, unit_fee = fee_table

    if parking_time_min <= basic_time:
        return basic_fee

    total_fee = basic_fee
    remain_time = parking_time_min - basic_time
    total_fee += (math.ceil(remain_time/unit_time)) * unit_fee

    return total_fee



fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))