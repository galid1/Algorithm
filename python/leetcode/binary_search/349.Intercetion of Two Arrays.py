# 브루트 포스 풀이
# class Solution:
#     def intersection(self, nums1, nums2):
#         ans = set()
#
#         for num in nums1:
#             if num in nums2:
#                 ans.add(num)
#
#         return list(ans)

# 이진탐색
# class Solution:
#     def intersection(self, nums1, nums2):
#         def is_in(num):
#             s, e = 0, len(nums2)-1
#             while s <= e:
#                 m = (s+e)//2
#                 if nums2[m] == num:
#                     return True
#                 elif nums2[m] > num:
#                     e = m-1
#                 else:
#                     s = m+1
#
#             return False
#
#         nums2.sort()
#
#         ans = set()
#         for num in nums1:
#             if is_in(num):
#                 ans.add(num)
#
#         return ans

# bisect 모듈
# import bisect
#
# class Solution:
#     def intersection(self, nums1, nums2):
#         result = set()
#         nums2.sort()
#
#         for n1 in nums1:
#             i2 = bisect.bisect_left(nums2, n1)
#             if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
#                 result.add(n1)
#
#         return result


class Solution:
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        L, R = 0, 0

        ans = set()
        while L < len(nums1) and R < len(nums2):
            if nums1[L] == nums2[R]:
                ans.add(nums1[L])
                L, R = L+1, R+1
            else:
                if nums1[L] < nums2[R]:
                    while L < len(nums1) and nums1[L] < nums2[R]:
                        L += 1
                else:
                    while R < len(nums2) and nums2[R] < nums1[L]:
                        R += 1
        return ans


s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
print(s.intersection(nums1, nums2))