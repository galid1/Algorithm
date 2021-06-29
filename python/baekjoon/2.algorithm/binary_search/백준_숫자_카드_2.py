# import sys
#
# def solution(cards, targets):
#     cards.sort()
#
#     answers = []
#     s = 0
#     for i in range(len(targets)):
#         answers.append(count(cards, targets[i]))
#
#     for a in answers:
#         print(a, end=' ')
#
#
# def count(cards, target):
#     s = 0
#     e = len(cards) - 1
#
#     start = None
#     while s <= e:
#         m = (s + e) // 2
#
#         if cards[m] > target:
#             e = m - 1
#         elif cards[m] < target:
#             s = m + 1
#         else:
#             start = m
#             break
#
#     # 찾는 수가 없음
#     if start is None:
#         return 0
#     else:
#         first = find_first(cards, target, start)
#         last = find_last(cards, target, start)
#         return last - first + 1
#
#
# def find_first(cards, target, start):
#     s = 0
#     e = start
#
#     first = None
#
#     while s <= e:
#         m = (s + e) // 2
#
#         if cards[m] > target:
#             e = m - 1
#         elif cards[m] < target:
#             s = m + 1
#         else:
#             first = m
#             e = m - 1
#
#     # start외에 target에 해당하는 수가 없다면 start를 first로 지정함
#     if first is None:
#         return start
#
#     return first
#
#
# def find_last(cards, target, start):
#     s = start
#     e = len(cards) - 1
#
#     last = None
#
#     while s <= e:
#         m = (s + e) // 2
#
#         if cards[m] > target:
#             e = m - 1
#         elif cards[m] < target:
#             s = m + 1
#         else:
#             last = m
#             s = m + 1
#
#     # 만약 start외에 target에 해당하는 수가 없다면 start를 last로 함
#     if last is None:
#         return start
#
#     return last

import sys
from collections import Counter

def solution(cards, targets):
    dic = dict(Counter(cards))

    answers = []
    for t in targets:
        if t in dic:
            answers.append(str(dic[t]))
        else:
            answers.append('0')

    answer = ' '.join(answers)
    print(answer)


n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split(" ")))
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split(" ")))
solution(cards, targets)