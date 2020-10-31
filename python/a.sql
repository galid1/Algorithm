문제 설명
다음과 같은 암호 알고리즘을 이용해 평문을 암호화해서 encrypted_text를 만들었습니다.

평문과 같은 길이의 문자열 key를 준비합니다.
암호화시킬 문장을 key를 이용해서 암호화시킵니다.
2번 결과로 나온 문장을 rotation만큼 회전시켜 줍니다.
예를 들어서 암호화시킬 문장이 hellopython이고, key가 abcdefghijk, rotation이 3이라고 하겠습니다.
먼저 암호화시킬 문장과 key를 이용해 다음과 같이 암호화해줍니다.

key에 있는 소문자 'a' ~ 'z'는 각각 순서대로 1~26까지의 숫자를 의미합니다.
평문의 각 알파벳을 key의 대응되는 위치에 있는 소문자가 나타내는 숫자만큼 뒤쪽에 나타나는 알파벳으로 바꿉니다.
예를 들어, 평문의 'e'에 대응되는 key의 알파벳이 'b'라면, 'e'에서 2만큼 뒤에 있는 알파벳 'g'로 바꾸면 됩니다.
이때 'z'를 넘어가는 문자는 다시 'a'부터 시작합니다. (xyz을 dbc로 암호화시키면 결과는 bac입니다)
위 방식대로 hellopython을 abcdefghijk을 이용해 암호화시키면 다음과 같이 igoptvfbqyy로 암호화됩니다.

'h' + 'a' = 'i' ('h'에서 1만큼 뒤에 있는 알파벳은 'i')
'e' + 'b' = 'g' ('e'에서 2만큼 뒤에 있는 알파벳은 'g')
...
'y' + 'g' = 'f' ('y'에서 7만큼 뒤에 있는 알파벳은 'f', 'z'를 넘어가므로 다시 'a'부터 시작)
...
'n' + 'k' = 'y' ('n'에서 11만큼 뒤에 있는 알파벳은 'y')
문자를 바꾼 후에는 다음과 같이 rotaion의 수치만큼 문자열을 회전시켜 줍니다. rotation 값이 양수면 오른쪽으로, 음수인 경우는 왼쪽으로 회전을 시켜 줍니다.

0 : igoptvfbqyy
1 : yigoptvfbqy
2 : yyigoptvfbq
3 : qyyigoptvfb
위와 같은 알고리즘으로 암호화된 문장 encrypted_text, 암호화에 사용된 key와 rotation이 매개변수로 주어질 때, 암호화를 하기 이전의 문장을 구해 return 하는 solution 함수를 완성해주세요.

제한사항
암호화된 문장 encrypted_text의 길이는 1 이상 1,000 이하입니다.
암호화된 문장 encrypted_text와 암호화되기 전 문장은 알파벳 소문자로만 구성되어 있습니다.
암호화에 사용되는 문장 key의 길이는 encrypted_text의 길이와 같으며, 알파벳 소문자로만 구성되어 있습니다.
회전 횟수 rotation은 -1,000 이상 1,000 이하의 정수입니다.
입출력 예
encrypted_text	key	rotation	result
qyyigoptvfb	abcdefghijk	3	hellopython
입출력 예 설명
문제의 예시와 같습니다.




문제 설명
CART_PRODUCTS 테이블은 장바구니에 담긴 상품 정보를 담은 테이블입니다. CART_PRODUCTS 테이블의 구조는 다음과 같으며, ID, CART_ID, NAME, PRICE는 각각 테이블의 아이디, 장바구니의 아이디, 상품 종류, 가격을 나타냅니다.

NAME	TYPE
ID	INT
CART_ID	INT
NAME	VARCHAR
PRICE	INT
문제
데이터 분석 팀에서는 상품 X를 샀을 때 상품 Y를 살 확률을 알아보려 합니다. 이를 위해 여러분은 서로 다른 두 아이템 쌍을 담은 장바구니 수를 구하려 합니다. 서로 다른 두 상품 X, Y을 동시에 담은 장바구니의 수를 조회하는 SQL 문을 작성해주세요. 상품 쌍을 담은 장바구니가 하나도 없는 경우, 이 상품 쌍에 대한 정보는 결과에 포함하지 않습니다. 또한 결과는 상품 X와 Y의 이름 순으로 보여주세요.

예시
예를 들어 CART_PRODUCTS 테이블이 다음과 같다면

CART_PRODUCTS 테이블

ID	CART_ID	NAME	PRICE
1632	83	Vegetable	2480
1633	83	Sausages	3980
1634	83	Vegetable	2480
5510	287	Vegetable	2480
5513	287	Sausages	3980
5514	287	Coffee	24800
(Vegetable, Sausages) 상품 쌍을 담은 장바구니는 83, 287번 장바구니 두 개 입니다.
(Sausages, Vegetable) 상품 쌍을 담은 장바구니는 83, 287번 장바구니 두 개 입니다.
(Vegetable, Coffee) 상품 쌍을 담은 장바구니는 287번 장바구니 하나입니다.
(Coffee, Vegetable) 상품 쌍을 담은 장바구니는 287번 장바구니 하나입니다.
(Sausages, Coffee) 상품 쌍을 담은 장바구니는 287번 장바구니 하나입니다.
(Coffee, Sausages) 상품 쌍을 담은 장바구니는 287번 장바구니 하나입니다.
결과는 상품 X와 Y의 이름 순으로 조회해야 하므로, SQL 문을 실행하면 다음과 같이 나와야 합니다.

NAME_X	NAME_Y	장바구니 수
Coffee	Sausages	1
Coffee	Vegetable	1
Sausages	Coffee	1
Sausages	Vegetable	2
Vegetable	Coffee	1
Vegetable	Sausages	2