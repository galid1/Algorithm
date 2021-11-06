def solution(log):
    acc_h, acc_m = 0, 0
    for i in range(0, len(log), 2):
        result = diff(log[i], log[i+1])

        if not valid(result[0], result[1]):
            continue

        if (result[0] == 1 and result[1] >= 45) or result[0] > 1:
            acc_h, acc_m = acc_h + 1, acc_m + 45
        else:
            acc_h, acc_m = acc_h + result[0], acc_m + result[1]

    acc_h += acc_m // 60
    acc_m %= 60
    acc_h, acc_m = str(acc_h), str(acc_m)

    ans_h = acc_h if len(acc_h) == 2 else '0' + acc_h
    ans_m = acc_m if len(acc_m) == 2 else '0' + acc_m

    return ans_h + ":" + ans_m


def diff(start, end):
    start_h, start_m = map(int, start.split(":"))
    end_h, end_m = map(int, end.split(":"))

    if start_m > end_m:
        end_h -= 1
        end_m += 60

    return end_h - start_h, end_m - start_m


def valid(h, m):
    if h == 0 and m < 5:
        return False

    return True



# print(diff('08:11', '09:00'))
# print(diff('07:00', '09:00'))
# print(diff('06:59', "06:59"))
# print(diff("01:01", "06:59"))

log = ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]
log = ["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]
print(solution(log))