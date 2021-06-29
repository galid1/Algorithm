def solution(n, stages):
    stages.sort(reverse=True)
    failures = {}

    next_idx = 0
    total = 0
    for i in range(n, 0, -1):
        not_cleared_cnt = 0
        cur_stage = i

        for j in range(next_idx, len(stages)):
            if stages[j] < cur_stage:
                next_idx = j
                break

            total += 1

            # 6같이 n보다 큰 경우는 5스테이지를 클리어한 상황임 때문에 total만 증가시키고 넘어감
            if stages[j] > cur_stage:
                continue

            not_cleared_cnt += 1

        if total == 0:
            failures[cur_stage] = 0
        else:
            failures[cur_stage] = (not_cleared_cnt/total)

    failures = dict(sorted(failures.items(), key = lambda item : item[0]))
    failures = dict(sorted(failures.items(), key= lambda item : item[1], reverse=True))

    answer = list(failures.keys())

    return answer

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4, 4, 4, 4, 4])