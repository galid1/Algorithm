from collections import Counter, defaultdict

def solution(research, n, k):
    greatest_condition = 2 * n * k
    research_map = {i:dict(Counter(research[i-1])) for i in range(1, len(research)+1)}
    issued_cnt = defaultdict(int)

    for start_day in range(1, len(research) + 2 - n):
        for keyword in research_map[start_day].keys():
            ## duration
            pass_day_condition = True
            total_search_cnt = 0

            for day in range(start_day, start_day + n):
                pass_day_condition = check_day_condition(day, keyword, k, research_map)

                # 당일 조건 불만족시 다음 키워드로
                if not pass_day_condition:
                    break

                total_search_cnt += research_map[day][keyword]

            if pass_day_condition and is_greatest(total_search_cnt, greatest_condition):
                issued_cnt[keyword] += 1

    issued_cnt = dict(sorted(issued_cnt.items(), key=lambda item: item[0], reverse=True))
    issued_cnt = dict(sorted(issued_cnt.items(), key=lambda item: item[1]))

    if len(issued_cnt) == 0:
        return "None"
    else:
        return issued_cnt.popitem()[0]

def check_day_condition(day, keyword, k, research_map):
    if keyword not in research_map[day].keys():
        return False

    return research_map[day][keyword] >= k


def is_greatest(total_search_cnt, greatest_condition):
    return total_search_cnt >= greatest_condition


research = ["abaaaa","aaa","abaaaaaa","fzfffffffa"]
n = 2
k = 2

research = ["yxxy","xxyyy"]
n = 2
k = 1

research = ["xy","xy"]
n = 1
k = 1

# research = ["yxxy","xxyyy","yz"]
# n = 2
# k = 1
print(solution(research, n, k))

# 당신은 검색 기능을 가진 사이트를 운영하고 있습니다. 당신은 매월 초마다 전월의 최고의 이슈 검색어를 조사하고 있습니다. 최고의 이슈 검색어를 조사하는 방법은 아래와 같습니다.
#
# 전월의 사용자들의 검색 기록을 일 기준으로 나눈 research가 주어집니다.
# research를 일 기준으로 어떤 검색어가 몇 번 검색되었는지 정리합니다.
# 어떤 검색어가 연속된 n일 동안 매일 최소 k 번 이상 검색되고, 같은 연속된 n일 동안 총 2 x n x k번 이상 검색되었을 경우 이슈 검색어가 됩니다.
# 예를 들어, n이 3이고 k가 50이면 그 전월에서 임의의 연속된 3일을 골랐을 때, 매일 50번 이상씩 검색되고 같은 기간 동안 총 300번 이상 검색되면 이슈 검색어가 됩니다.
# 이슈 검색어 중에서 가장 여러 번 이슈 검색어가 된 검색어가 최고의 이슈 검색어가 됩니다.
# 가장 여러 번 이슈 검색어가 된 검색어가 여러 개일 경우 사전 순으로 빠른 검색어가 최고의 이슈 검색어가 됩니다.
# 예를 들어, "a"가 2번 이슈 검색어가 되었고 "c"도 2번 이슈 검색어가 되었다면 "a"가 최고의 이슈 검색어가 됩니다.
# 그 전월의 사용자들의 검색 기록을 일 기준으로 나눈 1차원 문자열 배열 research, 정수 n, k가 매개변수로 주어집니다. 그 전월의 최고의 이슈 검색어를 조사하여 return 하도록 solution 함수를 완성해 주세요. 최고의 이슈 검색어가 없으면 "None"을 return해 주세요.
#
# 제한사항
# 2 ≤ research의 길이(=그 전월의 일 수) ≤ 30
# 2 ≤ research의 원소의 길이 ≤ 100
# research의 원소는 "검색어1검색어2..." 형태입니다. 하루 동안 검색된 검색어를 순서 없이 붙여 놓은 형태입니다.
# 검색어의 길이 = 1
# 검색어는 알파벳 소문자 중 하나입니다.
# 검색어는 서로 겹칠 수 있습니다.
# 예를 들어, "abaa"는 하루에 "a"가 3번 "b"가 1번 검색됐다는 뜻입니다.
# research에는 1일부터 하루 동안 검색된 검색어들이 차례대로 담겨져있습니다.
# 1 ≤ n ≤ research의 길이
# 1 ≤ k ≤ 100
# 입출력 예
# research	n	k	result
# ["abaaaa","aaa","abaaaaaa","fzfffffffa"]	2	2	"a"
# ["yxxy","xxyyy"]	2	1	"x"
# ["yxxy","xxyyy","yz"]	2	1	"y"
# ["xy","xy"]	1	1	"None"
# 입출력 예 설명
# 입출력 예 #1
#
# 총 4일 동안의 검색 기록이 주어졌습니다.
# 아래 표는 전월의 모든 검색어를 날마다 몇 번 검색되었는지 정리한 표입니다.
#
# 검색어	1일	2일	3일	4일
# a	5	3	7	1
# b	1	0	1	0
# f	0	0	0	8
# z	0	0	0	1
# 연속된 2(=n)일 동안 날마다 2(=k)번 이상 검색되고, 같은 연속된 2(=n)일 동안 총 8번(=2 x 2 x 2) 이상 검색된 검색어는 1일부터 2일까지 그리고 2일부터 3일까지 검색된 "a"뿐입니다. (4일에 k번 미만으로 검색되었으므로 3일부터 4일까지의 "a"는 이슈 검색어가 아닙니다.) 1일부터 2일까지 그리고 2일부터 3일까지 두 번 이슈 검색어가 된 "a"를 제외한 다른 검색어는 한 번도 이슈 검색어가 되지 못했습니다.
# 따라서 "a"를 return 합니다.
#
# 입출력 예 #2
#
# 총 2일 동안의 검색 기록이 주어졌습니다.
# 아래 표는 전월의 모든 검색어를 날마다 몇 번 검색되었는지 정리한 표입니다.
#
# 검색어	1일	2일
# x	2	2
# y	2	3
# 연속된 2(=n)일 동안 날마다 1(=k)번 이상 검색되고, 같은 연속된 2(=n)일 동안 총 4번(=2 x 2 x 1) 이상 검색된 검색어는 "x"와 "y"이고 두 검색어 모두 1일부터 2일까지 한 번만 이슈 검색어가 되었습니다.
# 따라서 사전 순으로 더 빠른 "x"를 return 합니다.
#
# 입출력 예 #3
#
# 총 3일 동안의 검색 기록이 주어졌습니다.
# 아래 표는 전월의 모든 검색어를 날마다 몇 번 검색되었는지 정리한 표입니다.
#
# 검색어	1일	2일	3일
# x	2	2	0
# y	2	3	1
# z	0	0	1
# 연속된 2(=n)일 동안 날마다 1(=k)번 이상 검색되고, 같은 연속된 2(=n)일 동안 총 4번(=2 x 2 x 1) 이상 검색된 검색어는 "x"와 "y"입니다. 이때 "x"는 1일부터 2일까지 단 한 번만 이슈 검색어가 되었고 "y"는 1일부터 2일까지 그리고 2일부터 3일까지 2번 이슈 검색어가 되었습니다.
# 따라서 더 많이 이슈 검색어가 된 "y"를 return 합니다.
#
# 입출력 예 #4
#
# 총 2일 동안의 검색 기록이 주어졌습니다.
# 아래 표는 전월의 모든 검색어를 날마다 몇 번 검색되었는지 정리한 표입니다.
#
# 검색어	1일	2일
# x	1	1
# y	1	1
# 연속된 1(=n)일 동안 날마다 1(=k)번 이상 검색되고, 같은 연속된 1(=n)일 동안 총 2번(=2 x 1 x 1) 이상 검색된 검색어는 없습니다.
# 따라서, 이슈 검색어가 없으므로 "None"을 return 합니다.