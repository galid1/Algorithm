# 문제 설명
# 다음과 같은 암호 알고리즘을 이용해 평문을 암호화해서 encrypted_text를 만들었습니다.
#
# 평문과 같은 길이의 문자열 key를 준비합니다.
# 암호화시킬 문장을 key를 이용해서 암호화시킵니다.
# 2번 결과로 나온 문장을 rotation만큼 회전시켜 줍니다.
# 예를 들어서 암호화시킬 문장이 hellopython이고, key가 abcdefghijk, rotation이 3이라고 하겠습니다.
# 먼저 암호화시킬 문장과 key를 이용해 다음과 같이 암호화해줍니다.
#
# key에 있는 소문자 'a' ~ 'z'는 각각 순서대로 1~26까지의 숫자를 의미합니다.
# 평문의 각 알파벳을 key의 대응되는 위치에 있는 소문자가 나타내는 숫자만큼 뒤쪽에 나타나는 알파벳으로 바꿉니다.
# 예를 들어, 평문의 'e'에 대응되는 key의 알파벳이 'b'라면, 'e'에서 2만큼 뒤에 있는 알파벳 'g'로 바꾸면 됩니다.
# 이때 'z'를 넘어가는 문자는 다시 'a'부터 시작합니다. (xyz을 dbc로 암호화시키면 결과는 bac입니다)
# 위 방식대로 hellopython을 abcdefghijk을 이용해 암호화시키면 다음과 같이 igoptvfbqyy로 암호화됩니다.
#
# 'h' + 'a' = 'i' ('h'에서 1만큼 뒤에 있는 알파벳은 'i')
# 'e' + 'b' = 'g' ('e'에서 2만큼 뒤에 있는 알파벳은 'g')
# ...
# 'y' + 'g' = 'f' ('y'에서 7만큼 뒤에 있는 알파벳은 'f', 'z'를 넘어가므로 다시 'a'부터 시작)
# ...
# 'n' + 'k' = 'y' ('n'에서 11만큼 뒤에 있는 알파벳은 'y')
# 문자를 바꾼 후에는 다음과 같이 rotaion의 수치만큼 문자열을 회전시켜 줍니다. rotation 값이 양수면 오른쪽으로, 음수인 경우는 왼쪽으로 회전을 시켜 줍니다.
#
# 0 : igoptvfbqyy
# 1 : yigoptvfbqy
# 2 : yyigoptvfbq
# 3 : qyyigoptvfb
# 위와 같은 알고리즘으로 암호화된 문장 encrypted_text, 암호화에 사용된 key와 rotation이 매개변수로 주어질 때, 암호화를 하기 이전의 문장을 구해 return 하는 solution 함수를 완성해주세요.
#
# 제한사항
# 암호화된 문장 encrypted_text의 길이는 1 이상 1,000 이하입니다.
# 암호화된 문장 encrypted_text와 암호화되기 전 문장은 알파벳 소문자로만 구성되어 있습니다.
# 암호화에 사용되는 문장 key의 길이는 encrypted_text의 길이와 같으며, 알파벳 소문자로만 구성되어 있습니다.
# 회전 횟수 rotation은 -1,000 이상 1,000 이하의 정수입니다.
# 입출력 예
# encrypted_text	key	rotation	result
# qyyigoptvfb	abcdefghijk	3	hellopython
# 입출력 예 설명
# 문제의 예시와 같습니다.


# 아스키 코드로
def to_ord(a):
    return (ord(a)-97)%26 + 1


# 알파벳으로
def to_chr(d):
    return chr((d - 1) % 26 + 97)


def r_rot(s, n):
    # for 말고, rotation 만큼 문자열을 잘라서 붙이는 방법도 있음 우선 이렇게
    if n > 0:
        for i in range(abs(n)):
            s = s[1:] + s[0]
    else: #-3 이었으니 다시 정방향으로
        for i in range(abs(n)):
            s = s[-1] + s[:-1]

    return s


def solution(encrypted_text, key, rotation):
    # 1. 역회전
    text = r_rot(encrypted_text, rotation)

    # 2. 역 움직임
    answer = ''
    for i in range(len(text)):
        answer += to_chr(to_ord(text[i]) - to_ord(key[i]))

    return answer


# print(solution('ebcd', 'aaaa', -3))
# print(solution('dddd', 'cccc', -2))
# print(solution("c", 'a', -1))
# print(solution('aap', 'abc', -5))
# print(solution('hello', 'abcde', 5))
# print(solution('bac', 'xyz', 0))
