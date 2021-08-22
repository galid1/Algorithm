class Solution:
    def searchMatrix(self, matrix, target):
        def is_in(target, row):
            s, e = 0, len(row)-1

            while s <= e:
                m = (s+e)//2
                if row[m] > target:
                    e = m-1
                elif row[m] < target:
                    s = m+1
                else:
                    return True

            return False

        row_i = 0
        while row_i < len(matrix) and matrix[row_i][0] <= target:
            if is_in(target, matrix[row_i]):
                return True
            row_i += 1

        return False



matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20

matrix = [[0]]
target = 0

s = Solution()
print(s.searchMatrix(matrix, target))
