import sys


def solution(s):
    nums = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
            'nine': '9'}

    answer = ''

    idx = 0
    while idx < len(s):
        if s[idx].isdigit():
            answer += s[idx]
            idx += 1
        else:
            word = ''
            while idx < len(s):
                word += s[idx]
                if word in nums:
                    answer += nums[word]
                    idx += 1
                    break
                idx += 1

    return answer

print(solution('one4seveneight'))