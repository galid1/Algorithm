# 1. 해시를 이용해 같은 종류는 같은 것끼리 묶음
# 2. 조합을 이용해 개수를 찾음
# 3. 모자: 1, 2, 상의 : a  하의: d, e 인 경우, 나올수 있는 조합은 아래와 같다
# 4. (1), (2), (a), (d), (e), (1,a), (2,a), (1,d), (1,e), (2,d), (2,e), (a,d), (a,e), (1,a,d), (1,a,e), (2,a,d), (2,a,e) = 17가지
# 5. 즉, 모자만 + 상의만 + 하의만 + (모자,상의) + (모자,하의) + (상의,하의) + (모자,상의,하의) 인 경우를 모두 더해야한다.
# 6. 이는 각 종류에 안입는 경우를 포함시켜 곱한뒤 -1 을 하면 구할수 있다 => 모자(3) * 상의(2) * 하의(3) - 1
# 7. -1을 하는 경우는 모두 안입는 경우를 제외하는 것 이다.

def solution(clothes):
    # 각 key(옷의 종류) 마다 배열을 만들어 저장
    dic = {}

    for cloth in clothes:
        if cloth[1] not in dic.keys():
            dic[cloth[1]] = set([cloth[0]])
        else:
            dic[cloth[1]].add(cloth[0])

    comb = 1
    for val in dic.values():
        comb = comb * (len(val) + 1)
    comb -= 1
    answer = comb

    return answer


# solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['yellow_sunglasses', 'eyewear'], ['green_turban', 'headgear'], ['red_hat', 'headgear']])
# solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
# solution([['1', 'a'], ['2', 'a'], ['3', 'a'], ['4', 'b'], ['5', 'b'], ['6', 'c'], ['7', 'c'], ['8', 'c'], ['9', 'c']])
solution([['1', 'a'], ['2', 'a'], ['3', 'a'], ['4', 'b'], ['5', 'c'], ['6', 'c'], ['7', 'c'], ['8', 'c']])