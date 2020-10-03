# 1. for i in 1 ~ len(n)//2
# 2. 반복자를 정함 (i 크기만큼)
# 3. 이전과 같으면 반복 수를 1증가 시킴
# 4. 이전과 다르면 1를 result에 더함(cnt가 1이상이면 1을 추가로 더함)
# 5. for문이 끝나고 cnt 크기가 1이상이면 조건에 따라 result에 추가로 더함
def solution(s):
    answer = []

    if len(s) == 1:
        return 1

    # 1부터 반까지만 (홀수인 경우 len/2, 짝수인 경우 len/2 -1 까지이므로 그냥 len/2+1 까지로)
    # 자르는 크기를 정함
    for i in range(1, len(s)//2+1):
        result = 0

        before_s = ''
        cnt = 1
        for cut_j in range(0, len(s), i):
            recur_s = s[cut_j:cut_j + i]

            # 첫 글자인 경우
            if not before_s:
                before_s = recur_s
                continue

            if before_s != recur_s:
                result += i
                if cnt > 1:
                    result += len(str(cnt))
                cnt = 1
            else:
                cnt += 1

            before_s = recur_s

        result += len(recur_s)
        if cnt > 1:
            result += len(str(cnt))

        answer.append(result)

    return min(answer)

# solution("aab")
# solution("aabbaccc")
solution('a')
# print(solution('ab'))
# solution("ababcdcdababcdcd")
# solution("abcabcdede")
# solution("abcabcabcabcdededededede")