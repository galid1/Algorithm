#백준 1463 1로 만들기
#import sys
# 입력된 수 x를 1로 만드는 문제
# 가능한 연산은 다음과 같다
# 1. x를 3으로 나눈다
# 2. x를 2로 나눈다
# 3. x에서 1을 뺀다

#dp 문제풀이
# 1. 항상 종료값을 우선 생각한다
# 2. 종료값이 정해지면 큰문제에서 작은 문제로가는 점화식을 생각해낸다


# 재귀 (recursive 제한에 걸림)
# def make_one(n):
#     if memo[n] >= 0:
#         return memo[n]
#
#     if n is 1 :
#         memo[n] = 0
#         return memo[n]
#     elif n <= 3:
#         memo[n] = 1
#         return memo[n]
#
#
#     min_num = 1000000
#     # 모든 경우를 다 해보아야 하므로 elif가 아닌 if로 함
#     if n%3 is 0:
#         min_num = min(min_num, 1 + make_one(int(n/3)))
#     if n%2 is 0:
#         min_num = min(min_num, 1 + make_one(int(n/2)))
#     min_num = min(min_num, 1 + make_one(n-1))
#     memo[n] = min_num
#     return memo[n]
#
# memo = [-1 for i in range(10000000)]
# n = int(sys.stdin.readline())
# print(make_one(n))

# bottom-up
# 정답
import sys

def make_one(n):
    if n <= 3:
        return memo[n]

    for i in range(4, n+1):
        min_num = memo[i - 1] + 1

        if i%3 == 0 :
            temp = memo[i//3] + 1
            min_num = min(min_num, temp)
        if i%2 == 0 :
            temp = memo[i//2] + 1
            min_num = min(min_num, temp)

        memo.append(min_num)

    return memo[n]

memo = [0,1,1,1]
n = int(sys.stdin.readline())
print(make_one(n))