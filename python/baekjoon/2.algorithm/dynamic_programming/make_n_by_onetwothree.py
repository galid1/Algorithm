#baekjoon 9095
#4는 1+3과 , 2+2, 3+1 로 표현이 가능하다(4는 사용할 수 없어 제외)
# 따라서 3을 만들수 있는방법 + 2를 만들수 있는방법 + 1을 만들 수 있는방법으로 계산이 된다
# 따라서 S(n) = S(n-1) + S(n-2) + S(n-3) 이다

# import sys
#
# def make_n(n):
#     if memo[n] > 0 :
#         return memo[n]
#
#     if n <= 3:
#         return memo[n]
#
#     for i in range(4, n+1):
#         memo[i]= memo[i-1] + memo[i-2] + memo[i-3]
#
#     return memo[n]
#
# memo = [0 for i in range(10002)]
# memo[1] = 1
# memo[2] = 2
# memo[3] = 4
#
# loop_num = int(sys.stdin.readline())
# result = []
# for i in range(loop_num):
#     n = int(sys.stdin.readline())
#     result.append(make_n(n))
#
# for i in result:
#     print(i)

# 15988 1,2,3 더하기 3
# n이 1,000,000까지의 조건으로 바뀜
# 알고리즘 자체가 O(N)이기 때문에 시간복잡도에는 걸리지 않지만 공간 복잡도에 걸림
# 따라서 배열을 순환하여 사용하도록 변경함 , 정답 출력시 정답을 1,000,000,009로 나눈 나머지를 출력
import sys

def make_n(n):
    if memo[n%len(memo)] > 0 :
        return memo[n%len(memo)]

    if n <= 3:
        return memo[n%len(memo)]

    for i in range(4, n+1):
        memo[i%len(memo)]= memo[(i-1)%len(memo)] + memo[(i-2)%len(memo)] + memo[(i-3)%len(memo)]

    return memo[n%len(memo)]

memo = [0 for i in range(12)]
memo[1] = 1
memo[2] = 2
memo[3] = 4

loop_num = int(sys.stdin.readline())
result = []
for i in range(loop_num):
    n = int(sys.stdin.readline())
    result.append(make_n(n))

for i in result:
    print(i%1000000009)