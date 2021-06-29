from collections import Counter

def solution(k, score):
    # 차이의 등수와 그 차이값을 묶은 사전
    dif_pair = {}
    dif = []
    for i in range(1, len(score)):
        dif_value = abs(score[i] - score[i-1])
        dif.append(dif_value)
        if dif_value not in dif_pair.keys():
            dif_pair[dif_value] = [(i, i+1)]
        else:
            dif_pair[dif_value].append((i, i+1))

    # 차이 수 구하기
    dif_dict = dict(Counter(dif))

    # k를 넘는 차이들 (key는 차이값, value는 차이 수)
    new_dif = {key:value for key,value in dif_dict.items() if value >= k}

    fake_grades = set()
    for key in new_dif.keys():
        for target_pair in dif_pair[key]:
            fake_grades.add(target_pair[0])
            fake_grades.add(target_pair[1])

    answer = len(score) - len(fake_grades)
    return answer


print(solution(3, [1,4,7,3,2,5,9,2,1]))
# solution(3, [24,22,20,10,5,3,2,1])
# solution(2, [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100])