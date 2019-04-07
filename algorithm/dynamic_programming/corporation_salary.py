#Topcoder SRM 407
import sys

def sum(relations):
    sum = 0
    for i in range(len(relations)):
        sum += salary(i, relations)
    return sum

def salary(num, relations):
    list = []
    for i in range(0, len(relations[0])):
        if relations[num][i] is 'Y':
            list.append(i)

    if len(list) is 0 :
        return 1

    sum = 0
    for i in list:
        sum += salary(i, relations)
    return sum


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    relations = []
    for i in range(n):
        relations.append(sys.stdin.readline())

    print(sum(relations))