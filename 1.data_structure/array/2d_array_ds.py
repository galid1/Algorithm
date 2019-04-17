#hackerrank 2D Array - DS
import math
import random
import re
import sys

# Complete the hourglassSum function below.
def add(num):
    return num + 1

def hourglassSum(arr):
    result = []
    list_x = [0,0,0,1,2,2,2]
    list_y = [0,1,2,1,0,1,2]

    for x in range(4):
        list_y = [0, 1, 2, 1, 0, 1, 2]
        for y in range(4):
            sum = 0
            for i in range(7):
                sum += arr[list_x[i]][list_y[i]]
            result.append(sum)
            list_y = list(map(add, list_y))
        list_x = list(map(add, list_x))
    return max(result)

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)