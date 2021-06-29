def solution(arr):
    total = 0
    for num in arr:
        total += num
    total /= len(arr)

    print(total)
    return total

solution([1, 2, 3, 4])
solution([5, 5])