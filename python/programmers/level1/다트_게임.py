def solution(results):
    t_ans = []

    cur_num = ''
    for i in range(len(results)):
        cur = results[i]

        if cur.isdigit():
            cur_num += cur

        elif cur in ['S', 'D', 'T']:
            if cur == 'D':
                t_ans.append(pow(int(cur_num), 2))
            elif cur == 'T':
                t_ans.append(pow(int(cur_num), 3))
            elif cur == 'S':
                t_ans.append(int(cur_num))
            cur_num = ''

        else:
            # 스타
            if cur == '*':
                t_ans[-1] *= 2
                if len(t_ans) > 1:
                    t_ans[-2] *= 2
            # 아차
            else:
                t_ans[-1] *= -1

    return sum(t_ans)

solution('1S2D*3T')
solution('1D2S#10S')
solution('1S*2T*3S')