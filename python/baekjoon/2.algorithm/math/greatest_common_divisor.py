import sys

## 간단한 풀이
#
# a, b = map(int, sys.stdin.readline().split(" "))
# g_num = 1
#
# for i in range(2, min(a,b)+1):
#     if a%i is 0 and b%i is 0 :
#         g_num = i
#
# print(g_num)

## 수학적 풀이
# 재귀적 유클리드 호제법
# def euclid(greatter, less):
#     if less == 0:
#         print(greatter)
#     else:
#         euclid(less, greatter%less)

# 반복문을 이용한 유클리드 호제법
a, b = map(int, sys.stdin.readline().split(" "))

def euclid(greatter, less):
    while less is not 0:
        temp = greatter
        greatter = less
        less = temp%less
    print(greatter)

greatter = max(a,b)
less = min(a,b)

euclid(greatter, less)