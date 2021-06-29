# 1. 짝수 대문자, 홀수 소문자
# 2. 공백기준 단어별로 짝수 홀수 인덱스 판별

# 1. 공백기준으로 단어를 나눔
# 2. 각 단어 별로 수행

def solution(s):
    s_list = s.split(" ")
    new_s_list = []

    for split_s in s_list:
        new_s = ''
        for i in range(len(split_s)):
            if i%2==0:
                new_s += split_s[i].upper()
            else:
                new_s += split_s[i].lower()

        new_s_list.append(new_s)

    answer = ''
    for k in range(len(new_s_list)):
        answer += new_s_list[k]
        if k != len(new_s_list) - 1:
            answer += ' '
    return answer

# print(solution('a'))
print(solution("try hello world"))
print("TrY HeLlO WoRlD")