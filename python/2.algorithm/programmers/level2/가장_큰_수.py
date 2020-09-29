# def solution(numbers):
#     numbers = list(map(str, numbers))
#
#     numbers_for_sort = []
#     # 모두 네자리로
#     for i in range(len(numbers)):
#         cur_num = numbers[i]
#         if len(cur_num) < 4:
#             need = 4 - len(cur_num)
#
#             for j in range(need):
#                 cur_num += cur_num[j]
#             numbers_for_sort.append([numbers[i], cur_num])
#         else:
#             numbers_for_sort.append([numbers[i], cur_num])
#
#     # 정렬
#     numbers_for_sort.sort(key= lambda x: x[1], reverse=True)
#
#     answer = ''.join(num[0] for num in numbers_for_sort)
#
#     # 모든 수가 0인경우, 문자열은 0000 이런식이지만 결국은 숫자이므로 0이어야함
#     answer = str(int(answer))
#
#     return answer

def solution(numbers):
    strs = list(map(str, numbers))

    strs.sort(key= lambda x: x*3, reverse=True)

    return str(int(''.join(strs)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([12, 121]))
print(solution([0, 0, 0, 0]))