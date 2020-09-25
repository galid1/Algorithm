# 1. 각 우선순위의 개수를 세서 dict에 저장, 가장 우선순위가 높은것을 기억
# 2. 프린터에서 뺀다,
# 2.1 현재 빼는 것이 가장 높은 우선순위보다 낮다면 제일 뒤로
# 2.2 우선순위가 가장 높다면, 뺀다
# - 빼낸 우선순위를 dict에서 제거, 가장 높은 것이었다면 다음 높은것으로 최신화
# - 내 프린트물 위치(location -= 1)
# - 출력순서 += 1
# - 내 프린트물이었다면 (location == 0) return answer

from collections import deque, Counter


def solution(priorities, locations):
    answer = 0
    #               {우선순위: 개수}
    prior_dic = dict(sorted(Counter(priorities).items(), key= lambda x: x[0], reverse=True))
    most_prior = tuple(prior_dic)[0]

    q = deque(priorities)

    while q:
        # 제일 앞의 대기열에서 빼내어 판별
        cur = q.popleft()
        locations -= 1

        # 제일 높은 우선순위를 뽑은 경우
        if cur >= most_prior:
            # 출력 번호 1증가
            answer += 1

            # 정답
            if locations == -1:
                break

            # 우선순위 최신화
            prior_dic[cur] -= 1
            if prior_dic[cur] == 0:
                prior_dic.pop(cur)
                most_prior = tuple(prior_dic)[0]
        else:
            # 내가 뽑을 출력물인 경우 제일 뒤로
            if locations == -1:
                locations = len(q)

            q.append(cur)

    return answer


solution([2,1,3,2], 2)
# solution([1,1,9,1,1,1], 0)