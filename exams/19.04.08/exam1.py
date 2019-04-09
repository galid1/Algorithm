import sys
import queue

def isPangram(strings):
    results = []
    # 문자열 담기
    strs = []
    for str1 in strings:
        list_str = list(str1)
        strs.append(list_str)

    for str2 in strs:
        dict = {'a': '1', 'b': '2', 'c': 3, 'd': 4, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1,
                'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}

        flag = False
        for i in range(0, len(str2)):
            if len(dict) == 0:
                results.append(1)
                flag = True
                break

            if str2[i] in dict:
                dict.pop(str2[i])
        if len(dict) == 0 and not flag:
            results.append(1)
        if len(dict) > 0:
            results.append(0)

    result_str = ''
    for j in results:
        result_str += str(j)

    return result_str




if __name__ == '__main__':

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    result = isPangram(strings)