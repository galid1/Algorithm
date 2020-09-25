# 백준 1874 스택 수열

import sys

# 1. 만들어야하는 순열의 현재 인덱스번째의 수와 일치할때까지 1~n에서(반대로 뒤집은) pop() 한뒤 stack에 push , answer에 "+" push
# 2. 만들어야하는 순열의 현재 인덱스번째의 수와 일치할때까지 stack에서 pop(), answer에 "-" push
# 3. 다음 인덱스 수가 방금 pop한 수보다 작으면 더 pop() 높으면 그만

# def solution():
#     answer = []
#     stack = []
#
#     permu_idx = -1
#     num_idx = 1
#
#     while permu_idx < len(permu):
#         # 다음 출력해야하는 수열의 수의 인덱스
#         permu_idx += 1
#
#         # 출력해야 하는 수까지 stack에 push
#         for i in range(num_idx, len(permu)+1):
#             stack.append(i)
#             answer.append("+")
#             num_idx += 1
#
#             if permu[permu_idx] == i:
#                 break
#
#         # 출력해야 하는 수까지 stack에서 pop
#         pop_num = 0
#         while stack:
#             pop_num = stack.pop()
#             answer.append('-')
#             if pop_num == permu[permu_idx]:
#                 break
#
#         if permu_idx + 1 < len(permu):
#             # 다음수가 방금 출력한수보다 작다면 계속 pop
#             while permu_idx + 1 < len(permu):
#                 if pop_num < permu[permu_idx+1]:
#                     break
#
#                 permu_idx += 1
#                 pop_num = stack.pop()
#                 answer.append('-')
#
#                 if pop_num != permu[permu_idx]:
#                     print("NO")
#                     return
#
#     for a in answer:
#         print(a)

def solution():
    answer = []
    stack = []
    num = 0
    permu_idx = 0

    while permu_idx < len(permu):
        while num < permu[permu_idx]:
            num += 1
            stack.append(num)
            answer.append('+')

        if stack[-1] == permu[permu_idx]:
            stack.pop()
            answer.append('-')
            permu_idx += 1
        else:
            print('NO')
            return

    for a in answer:
        print(a)


permu = []
n = int(sys.stdin.readline())
for i in range(n):
    permu.append(int(sys.stdin.readline()))
solution()