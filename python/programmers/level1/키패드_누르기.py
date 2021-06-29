def solution(numbers, hand):
    answer = ''
    l = -1
    r = -1

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            l = num
        elif num in [3, 6, 9]:
            answer += 'R'
            r = num
        else:
            center_nums = [2, 5, 8, 0]
            # 현재 왼손 오른손 위치 복사
            lt = l
            rt = r
            # 손의 이동 회수
            ld = 0
            rd = 0

            # 왼손 가운데로
            if lt in [1, 4, 7]:
                lt += 1
                ld += 1
            elif lt == -1:
                lt = 0
                ld += 1

            # 오른손 가운데로
            if rt in [3, 6, 9]:
                rt -= 1
                rd += 1
            elif rt == -1:
                rt = 0
                rd += 1

            ld += abs(center_nums.index(lt) - center_nums.index(num))
            rd += abs(center_nums.index(rt) - center_nums.index(num))

            if ld > rd:
                answer += 'R'
                r = num
            elif rd > ld:
                answer += 'L'
                l = num
            else:
                if hand == 'left':
                    answer += 'L'
                    l = num
                else:
                    answer += 'R'
                    r = num
    return answer

# solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")