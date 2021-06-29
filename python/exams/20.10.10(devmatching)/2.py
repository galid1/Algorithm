def solution(p, n):
    # 1. 일자를 다 없앰
    n = n%86400
    # 2. 시분초 계산
    h = n // 3600
    n %= 3600
    m = n // 60
    s = n % 60

    time_split = p.split(" ")
    typ =  time_split[0]
    target_time = time_split[1]

    target_time_split = target_time.split(":")
    target_h = target_time_split[0]
    target_m = target_time_split[1]
    target_s = target_time_split[2]


    target_s = int(target_s) + int(s)
    re_target_s = target_s//60
    target_s %= 60

    target_m = int(target_m) + int(m) + re_target_s
    re_target_m = target_m//60
    target_m %= 60

    target_h = int(target_h) + int(h) + re_target_m
    if target_h >= 12:
        target_h -= 12

        if typ == 'AM':
            typ == 'PM'
        else:
            typ == 'AM'

    if len(str(target_h)) == 1:
        target_h = '0' + str(target_h)
    if len(str(target_m)) == 1:
        target_m = '0' + str(target_m)
    if len(str(target_s)) == 1:
        target_s = '0' + str(target_s)

    answer = ''
    if typ == 'AM':
        answer = str(target_h) + ":" + str(target_m) + ":" + str(target_s)
    else:
        answer = str(12 + int(target_h)) + ":" + str(target_m) + ":" + str(target_s)

    return answer


print(solution('PM 01:00:40', 59))