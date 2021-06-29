def solution(s):
    answer = ''

    nums = list(map(int, s.split(" ")))

    max_num = max(nums)
    min_num = min(nums)
    answer = str(min_num) + ' ' + str(max_num)

    return answer

solution("1 2 3 4")
solution("-1 -2 -3 -4")