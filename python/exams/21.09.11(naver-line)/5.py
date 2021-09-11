문제
설명
브라운은
자신이
만든
모바일
게임에, 이벤트
참여를
위해
동일한
유저가
여러
닉네임과
이메일로
중복
가입했다는
제보를
받았습니다.고심하던
브라운은
다음과
같은
기준으로
두
유저가
동일한
유저인지
판단하려고
합니다.

어떤
두
유저의
닉네임과
이메일
주소가
모두
유사하면
동일한
유저라고
판단합니다.또한(a, b)
가
동일
유저이고(b, c)
가
동일
유저라면, (a, c)
는
동일
유저라고
간주합니다.

[I.닉네임 유사성 판단 기준]

어떤
두
닉네임에서, 총
2
개
이하의
문자를
삭제하여
동일하게
만들
수
있다면
두
닉네임은
유사하다고
판단합니다.
imhero111, imher1111은
각각
하나의
문자를
삭제하여
동일하게
만들
수
있으므로, 유사한
닉네임입니다.
imhero111
imher1111
imhero111, hero111은
첫
닉네임에서
두
개의
문자를
삭제하여
동일하게
만들
수
있으므로, 유사한
닉네임입니다.
imhero111
hero111
money55man, moneymann은
다음과
같이
최소
3
개의
문자를
삭제해야만
동일하게
만들
수
있으므로, 유사한
닉네임이
아닙니다.
money55man
moneymann
[II.이메일 주소 유사성 판단 기준]

이메일
주소는 @ 기호
앞부분인
계정이름과
뒷부분인
서버이름으로
나누어집니다.

예) ace12Boy @ abcd.com
ace123Boy가
계정이름이며, abcd.com이
서버이름입니다.
    다음
2
개의
조건
중, 하나
이상에
해당하면
유사한
이메일이라고
판단합니다.

    어떤
두
이메일
주소의
계정이름에서, 총
1
개의
문자를
삭제하여
전체
이메일
주소를
동일하게
만들
수
있으면
유사하다고
판단합니다.
    superman5 @ abcd.com, superyman5 @ abcd.com은
계정이름에서
총
1
개의
문자를
삭제하여
전체
이메일
주소를
동일하게
만들
수
있으므로
유사한
이메일입니다.
    superman5 @ abcd.com
superyman5 @ abcd.com
aaabaaa @ qwer.pe, aaaaaa @ abcd.pe는
계정이름
부분만
놓고
보면
1
개의
문자를
삭제하여
동일하게
만들
수
있지만, 서버이름이
달라서
전체
이메일
주소가
같아질
수
없으므로, 유사한
이메일이
아닙니다.
    aaabaaa @ qwer.pe
aaaaaa @ abcd.pe
어떤
두
이메일
주소의
계정이름이
동일하면, 서버이름과
상관없이
유사하다고
판단합니다.
    superman @ abcd.com, superman @ erty.net은
서버이름은
다르지만, 계정이름이
동일하므로
유사한
이메일
주소입니다.
    superman @ abcd.com
superman @ erty.net
브라운이
만든
모바일
게임에
가입된
유저들의
닉네임이
담긴
문자열
배열
nicks, 이메일
주소가
담긴
문자열
배열
emails가
매개변수로
주어집니다.위에서
주어진
기준으로
동일
유저를
판단했을
때, 실제로
가입한
유니크(Unique)
유저의
수를
return 하도록
solution
함수를
완성해주세요.

제한사항
nicks에는
1
번
유저의
닉네임부터
차례대로
담겨있습니다.
1 ≤ nicks의
길이 ≤ 100
3 ≤ nicks의
원소의
길이 ≤ 20
nicks의
원소는
알파벳
소문자와
숫자로만
이루어진
문자열입니다.
nicks에
중복된
원소는
담겨있지
않습니다.즉, 모든
닉네임은
서로
다릅니다.
emails에는
1
번
유저의
이메일
주소부터
차례대로
담겨있습니다.
emails의
길이 = nicks의
길이
9 ≤ emails의
원소의
길이 ≤ 41
emails의
원소는
알파벳
소문자, 숫자, 특수문자('@', '.')
로만
이루어진
문자열입니다.
emails의
각
원소에서, '@'
는
정확히
1
번만
등장합니다.
emails의
각
원소는
"계정이름@서버이름"
형식입니다.
3 ≤ 계정이름의
길이 ≤ 20
계정이름은
알파벳
소문자와
숫자로만
이루어진
문자열입니다.
5 ≤ 서버이름의
길이≤ 20
서버이름은
알파벳
소문자와
특수문자('.')
로만
이루어진
문자열입니다.
emails에
중복된
원소는
담겨있지
않습니다.즉, 모든
이메일은
서로
다릅니다.
emails에
담긴
모든
이메일
주소는
올바른
형식의
이메일
주소라고
가정합니다.
입출력
예
nicks
emails
result
["imhero111", "moneyman", "hero111", "imher1111", "hro111", "mmoneyman", "moneymannnn"][
    "superman5@abcd.com", "batman432@korea.co.kr", "superman@abcd.com", "supertman5@abcd.com", "superman@erty.net", "batman42@korea.co.kr", "batman432@usa.com"]
3
["99police", "99poli44"]["687ufq687@aaa.xx.yyy", "87ufq687@aaa.xx.yyy"]
2
["99polico", "99policd"]["687ufq687@aaa.xx.yyy", "587ufq687@aaa.xx.yyy"]
2
입출력
예
설명
입출력
예  # 1

닉네임
이메일
주소
imhero111
superman5 @ abcd.com
hero111
superman @ abcd.com
1, 3
번
유저는
동일
유저입니다.

닉네임
이메일
주소
imhero111
superman5 @ abcd.com
imher1111
supertman5 @ abcd.com
1, 4
번
유저는
동일
유저입니다.

닉네임
이메일
주소
hero111
superman @ abcd.com
hro111
superman @ erty.net
3, 5
번
유저는
동일
유저입니다.

닉네임
이메일
주소
moneyman
batman432 @ korea.co.kr
mmoneyman
batman42 @ korea.co.kr
2, 6
번
유저는
동일
유저입니다.

7
번
유저와
동일한
유저는
없습니다.

즉, 유니크
유저는[(1, 3, 4, 5), (2, 6), (7)]
3
명입니다.

입출력
예  # 2

닉네임
이메일
주소
99
police
687u
fq687 @ aaa.xx.yyy
99
poli44
87u
fq687 @ aaa.xx.yyy
이메일
주소는
계정이름에서
단
하나의
문자를
삭제하여
전체
이메일
주소를
동일하게
만들
수
있으므로, 유사하다고
판단할
수
있습니다.
하지만, 닉네임은
최소
4
개의
문자를
삭제해야만
동일하게
만들
수
있으므로, 유사하지
않다고
판단합니다.
따라서, 1, 2
번
유저는
동일한
유저가
아닙니다.
입출력
예  # 3

닉네임
이메일
주소
99
polico
687u
fq687 @ aaa.xx.yyy
99
policd
587u
fq687 @ aaa.xx.yyy
닉네임은
2
개의
문자를
삭제하여
전체
이메일
주소를
동일하게
만들
수
있으므로, 유사하다고
판단할
수
있습니다.
하지만, 이메일
주소는
계정이름에서
2
개의
문자를
삭제해야만
동일하게
만들
수
있으므로, 유사하지
않다고
판단합니다.
닉네임과
이메일
주소의
유사성을
판단하는
기준은
상이함을
주의해주세요.
따라서, 1, 2
번
유저는
동일한
유저가
아닙니다.