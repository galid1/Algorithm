# two pointer 풀이
# class Solution:
#     def twoSum(self, numbers, target):
#         L, R = 0, len(numbers)-1
#
#         while L < R:
#             sums = numbers[L] + numbers[R]
#             if sums > target:
#                 R -= 1
#
#             elif sums < target:
#                 L += 1
#
#             else:
#                 return L+1, R+1

# 이진탐색 풀이
class Solution:
    def twoSum(self, numbers, target):
        for idx, num in enumerate(numbers):
            cur_target = target - num

            L, R = idx+1, len(numbers)-1

            while L <= R:
                m = (L+R)//2

                if numbers[m] > cur_target:
                    R = m-1
                elif numbers[m] < cur_target:
                    L = m+1
                else:
                    return idx+1, m+1



# 조건 : 하나의 정답은 꼭 존재 !

s = Solution()
numbers = [2,7,11,15]
target = 9

print(s.twoSum(numbers, target))