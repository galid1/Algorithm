num_arr = [5, 3, 1, 4, 2]

for i in range(1, len(num_arr)):
    temp = num_arr[i]
    for j in range(i - 1, -1, -1):
        changed = False

        if temp < num_arr[j]:
            num_arr[j + 1] = num_arr[j]
            changed = True
        else:
            num_arr[j + 1] = temp
            break

        if changed and j == 0:
            num_arr[j] = temp

    for num in num_arr:
        print(num, end= " ")
    print()
