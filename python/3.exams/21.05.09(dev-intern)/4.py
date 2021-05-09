# 문제 설명
# FRIENDS 테이블은 SNS 내 친구 관계 정보를 담고 있습니다. FRIENDS 테이블 구조는 다음과 같으며 ID1, ID2 쌍은 ID1과 ID2가 서로 친구라는 뜻입니다.
#
# NAME	TYPE	NULLABLE
# ID1	VARCHAR(N)	FALSE
# ID2	VARCHAR(N)	FALSE
# 이 테이블에서, 친구 관계는 양방향이며, 친구 관계가 중복으로 등록되는 경우는 없습니다. 예를 들어, id1가 id2의 친구이면 id2는 id1의 친구이고, 레코드 id1, id2가 등록되어 있을 때, 레코드 id2, id1가 등록된 경우는 없습니다.
#
# 문제
# FRIENDS 테이블에 등록된 모든 유저에 대해, 각 유저의 친구가 몇 명인지 조회하는 SQL을 작성해주세요. 이때 결과는 ID 순으로 정렬되어야 합니다.
#
# 예시
# 예를 들어, FRIENDS 테이블이 다음과 같다면
#
# ID1	ID2
# processornoe1303	aboriginalvader565
# aboriginalvader565	lomojubilee1357
# aboriginalvader565의 친구는 2명(processornoe1303, lomojubilee1357)
# lomojubilee1357의 친구는 1명(aboriginalvader565)
# processornoe1303의 친구는 1명(aboriginalvader565)
# 이기 때문에 SQL을 실행하면 다음과 같이 출력되어야 합니다.
#
# ID	COUNT
# aboriginalvader565	2
# lomojubilee1357	1
# processornoe1303	1