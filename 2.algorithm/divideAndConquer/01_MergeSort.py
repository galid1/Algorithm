def divide(start, end, list):
    if start < end :
        center = int((start + end)/2)
        divide(start, center, list)
        divide(center+1, end, list)
        conquer(start, center, end, list)

def conquer(start, center, end, list):
    new_list = []
    i = start
    j = center + 1

    while i <= center and j <= end:
        if list[i] <= list[j]:
            new_list.append(list[i])
            i += 1
        else:
            new_list.append(list[j])
            j += 1

    # i가 center보다 크다는 것은 i는 이미 모든 수가 사용됬다는 것 따라서 j를 그대로 붙힌다
    # start가 center와 같은 경우에는 수를 사용하지 않았음에도 수를 다 사용한것 처럼 인식 되기 때문에 start is not center 조건이 동시에 부합되야 함
    if i > center:
        while j <= end:
            new_list.append(list[j])
            j += 1
    # 그렇지 않은 경우는 j범위의 모든 수가 사용된 것 따라서 i를 그대로 붙힌다
    else:
        while i <= center:
            new_list.append(list[i])
            i += 1

    # 실제 배열에 정렬된 값 담기
    k = 0
    for i in range(start, end+1):
        list[i] = new_list[k]
        k += 1

if __name__=="__main__":
    none_sort_str = input().split(" ")
    none_sort_list = list(map(int, none_sort_str))
    divide(0, len(none_sort_list)-1, none_sort_list)
    print(none_sort_list)