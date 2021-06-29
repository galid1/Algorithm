from collections import Counter

def solution(votes, k):
    answer = ''

    votes_dict = dict(Counter(votes))
    alpha_sorted_votes_dict = dict(sorted(votes_dict.items(), key = lambda item: item[0], reverse=True))
    sorted_votes_dict = dict(sorted(alpha_sorted_votes_dict.items(), key = lambda item: item[1]))

    # 상위 득표수 합 구하기
    limit_li = list(sorted_votes_dict.values())
    limit = 0
    for i in range(len(sorted_votes_dict)-1, len(sorted_votes_dict)- 1 - k, -1):
        limit += limit_li[i]

    # 탈락 차 구하기
    sums = 0
    before_key = ''
    for key in sorted_votes_dict.keys():
        if sums + sorted_votes_dict[key] >= limit:
            answer = before_key
            break

        sums += sorted_votes_dict[key]
        before_key = key

    return answer


# solution(["AVANT", "PRIDO", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "AVANT", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "SOULFUL", "AVANT", "SANTA"], 2)
solution(["AAD", "AAA", "AAC", "AAB"], 4)