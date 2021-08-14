from itertools import combinations

def solution(fruitWeights, k):
    lists = []
    for i in range(len(fruitWeights)):
        if i < len(fruitWeights)-2:
            lists.append([fruitWeights[i], fruitWeights[i+1], fruitWeights[i+2]])

    print(lists)


# fruits = [30, 40, 10, 20, 30]
fruits = [10, 50, 20, 40, 20, 30]
k = 3
print(solution(fruits, k))