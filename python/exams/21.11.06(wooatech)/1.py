from collections import Counter

def solution(arr):
    answer = [0 for _ in range(4)]
    cnts = dict(Counter(arr))

    max_cnt = max(cnts.values())
    for key in (1, 2, 3):
        if key not in cnts.keys():
            answer[key] = max_cnt
        else:
            answer[key] = (max_cnt - cnts[key])

    return answer[1:]


arr = [2, 1, 3, 1, 2, 1]
arr = [3, 3, 3, 3, 3, 3]
arr = [1]
print(solution(arr))