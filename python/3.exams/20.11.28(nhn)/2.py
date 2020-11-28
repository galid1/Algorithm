page = 5457
broken = [6, 7, 8]
# page = 99999
# broken = [0, 2, 3, 4, 5, 6, 7, 8, 9]

def solution():
    global page, broken
    start_page = 100

    # + 혹은 - 로만 움직이는 경우
    answer = abs(page - start_page)

    # 숫자버튼 함께 사용하는 경우
    non_broken = set(i for i in range(10)).difference(broken)
    for i in range(1000001):
        use_broken = False
        # 고장난 버튼을 사용하는지 확인
        for sub in str(i):
            if int(sub) not in non_broken:
                use_broken = True
                break

        if not use_broken:
            answer = min(answer, abs(page - i) + len(str(i)))

    return answer


print(solution())