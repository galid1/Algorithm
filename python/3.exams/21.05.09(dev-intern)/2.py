def solution(t, r):
    answer = []

    # t, idx, r
    infos = make_infos(t, r)

    time = 0
    while infos:
        # print("====")
        # print('infos : ', infos)
        # 기준
        ct, ci, cr = infos[0]
        # print('ct, ci, cr : ', ct, ci, cr)

        # 원소가 하나 남음
        if len(infos) == 1:
            answer.append(infos.pop()[1])
            continue

        if ct > time:
            time += 1
            continue

        idx = 1
        del_idx = 0
        while idx < len(infos):
            if infos[idx][0] > time:
                idx -= 1
                break

            if cr > infos[idx][2]:
                del_idx = idx
                ct, ci, cr = infos[idx]
            idx += 1

        answer.append(ci)
        del(infos[del_idx])

        time += 1

    return answer


def make_infos(t, r):
    infos = []
    for i in range(len(t)):
        data = (t[i], i, r[i])
        infos.append(data)

    infos.sort(key=lambda e: e[1])
    infos.sort(key=lambda e: e[0])

    return infos


t = [0, 1, 3, 0]
r = [0, 1, 2, 3]
# t = [1,1,1,1]
# r = [4,1,1,3]

t = [7,6,8,1]
r = [0,1,2,3]
solution(t, r)
