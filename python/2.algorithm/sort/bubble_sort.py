def bubble_sort(num_arr):
    for i in range(len(num_arr) - 1, 0, -1):
        changed = False
        for j in range(0, i, +1):
            if num_arr[j] > num_arr[j + 1]:
                temp = num_arr[j]
                num_arr[j] = num_arr[j + 1]
                num_arr[j + 1] = temp
                changed = True

        if not changed:
            return

num_arr = [6, 3, 2, 1, 4, 5]
bubble_sort(num_arr)

for num in num_arr:
    print(num)