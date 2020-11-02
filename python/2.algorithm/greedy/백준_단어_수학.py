import sys


def solution():
    global n, arr, dic

    # 그리디를 위해 각 글자가 위치한 곳중 제일 큰것을 찾아 정렬
    for word in arr:
        for i in range(len(word)):
            a = word[i]

            dic[a] += pow(10, len(word)-i-1)
    dic = dict(sorted(dic.items(), key= lambda items: items[1], reverse=True))

    # 정렬된 순서에 맞추어 수를 맵핑
    map_num = 9
    for k in dic.keys():
        dic[k] = map_num
        map_num -= 1

    # 단어들을 수로 맵핑하고 결과에 더함
    answer = 0
    for arr_idx in range(len(arr)):
        res = 0
        word = arr[arr_idx]
        for word_idx in range(len(word)):
            res += dic[word[word_idx]] * pow(10, len(word) - word_idx - 1)

        answer += res

    print(answer)


n = int(sys.stdin.readline())
dic = {chr(65 + i): 0 for i in range(26)}
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())
solution()