num_arr = [6, 3, 5, 4, 1, 2]

for i in range(0, len(num_arr) - 1):
    min_num_idx = i+1
    for j in range(i + 2, len(num_arr)):
        if num_arr[min_num_idx] > num_arr[j]:
            min_num_idx = j

    if num_arr[i] > num_arr[min_num_idx]:
        temp = num_arr[i]
        num_arr[i] = num_arr[min_num_idx]
        num_arr[min_num_idx] = temp

    print(i, "회전 결과 @@@@@@@@@@")
    for num in num_arr:
        print(num, end = " ")


