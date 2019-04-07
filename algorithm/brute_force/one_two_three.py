import sys
### 1,2,3 을 더하여 n을 만든다 (n <= 10) 중복 덧셈 허용
### ex) n = 3 => (1,1,1) , (1,2) , (2,1) , (3)

## n중 for 문
# n =  int(sys.stdin.readline())
# count = 0
# for i in range(1, 4):
#     if i is n:
#         count += 1
#         continue
#
#     for j in range(1, 4):
#         if i+j is n:
#             count += 1
#             continue
#
#         for k in range(1, 4):
#             if i+j+k is n:
#                 count += 1
#                 continue
# print(count)

## 재귀함수
def use_one_two_three(n, current_sum = 0):
    global count
    if current_sum is n:
        count += 1
        return
    if current_sum > n :
        return
    for i in range(1, 4):
        use_one_two_three(n, current_sum + i)

count = 0
n = int(sys.stdin.readline().strip())
use_one_two_three(n)
print(count)