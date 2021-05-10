def d(num):
    global v

    next_num = num

    while True:
        tmp = 0
        for i in range(len(str(next_num))):
            tmp += int(str(next_num)[i])
        tmp += next_num

        if tmp > 10000 or v[tmp] or tmp == num:
            break

        next_num = tmp
        v[next_num] = True



v = [False for _ in range(10001)]

# 1부터 반복하며 d(i)를 구해서, v에 추가
for i in range(1, 9999):
    d(i)

# 정답 출력
for j in range(1, 10001):
    if not v[j]:
        print(j)