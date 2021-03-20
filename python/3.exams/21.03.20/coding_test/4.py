# 문제 설명
# 라인 인형 판매 사이트는 인형의 이름과 특징을 담은 데이터(data)를 활용하여 사이트를 운영하고 있습니다.
#
# data는 다음과 같은 성질을 가진 자료구조입니다.
#
# 한 개 이상의 트리로 이루어진 구조입니다.
# 각 노드의 구성 요소는 노드의 ID, 인형의 이름 혹은 특징, 그리고 부모 노드의 ID 등 세 가지입니다.
# 각 리프 노드(leaf node)1에는 인형의 이름이 담겨 있습니다.
# 각 내부 노드(non-leaf node)에는 인형의 특징이 담겨 있습니다.
# 인형 이름(리프 노드)의 조상 노드들은2 그 인형의 특징을 나타냅니다.
# Untitled Diagram.jpg
#
# 위 그림은 data의 이해를 돕기위한 그림입니다. 인형1은 특징1을 가지고있습니다. 인형2와 인형3은 특징1과 특징2를 가지고 있습니다.
#
# 당신은 data를 활용하여 검색창에 검색어(word)를 입력하면, 인형 이름에 word를 포함한 인형들의 이름(리프 노드)과 특징(조상 노드)을 한 번에 볼 수 있게 아래와 같은 순서로 검색 기능을 개발하려고 합니다.
#
# 검색 조건은 다음과 같습니다.
#
# 인형 이름이 word와 정확히 일치하는 인형을 가장 먼저 검색합니다.
# 인형 이름에 word가 많이 포함될수록 먼저 검색합니다.
# 인형 이름에 포함된 word 개수가 같으면 인형 이름 안에 word가 앞에 있을수록 먼저 검색합니다.
# 만약 첫 번째 word가 등장하는 위치가 같다면 계속해서 다음 word의 위치를 비교합니다.
# 예를 들어 word가 "AA"이고 인형 이름이 "AABAA", "AABBAA" 인 경우, "AABAA"를 먼저 검색합니다.
# 검색 순위가 같다면 ID 가 더 작은 인형을 먼저 나열합니다.
# 인형 이름에서 word를 찾을 때 알파벳은 한 번씩만 셉니다. 예를 들어, 인형 이름이 "AAA"이고 word가 "AA"이면 word가 맨 앞에 하나 포함되어있는 것입니다. 인형 이름의 2번째 A를 두 번 세어 word가 2번 포함되어 있는 것이 아님을 유의하세요.
#
# 검색 결과는 인형의 특징도 보여줘야 하므로 검색된 인형의 이름 앞에 인형의 특징(인형의 조상 노드들)을 루트 노드부터 차례대로 /로 구분하여 만든 문자열을 담은 배열이어야 합니다. 즉, 검색 결과의 원소는 "검색한 인형의 루트 노드의 인형 특징/ ... /검색한 인형의 부모 노드의 인형 특징/검색한 인형 이름" 의 형식이어야 합니다. 예를 들어, word가 CUTE일 때, 검색된 인형 이름이 CUTE-CONY 하나라면 검색 결과는 ["DOLL/CONY/CUTE-CONY"]와 같이 인형 이름 앞에 특징이 붙은 형식이어야 합니다. 조상 노드가 없는 경우는 인형의 이름만 검색 결과에 담습니다.
#
# 인형 데이터를 담은 문자열 배열 data와 검색어 word가 매개변수로 주어집니다. word로 검색했을 때, 검색 결과를 검색 순서와 형식에 맞추어 배열에 담아 return 하도록 solution 함수를 완성해주세요. 검색 조건에 맞는 데이터가 없을 경우 "Your search for (word) didn't return any results"를 배열에 담아 return 해주세요.
#
# 제한 사항
#
# 2 ≤ data의 길이 ≤ 1,000
# data의 원소는 "ID NAME PARENT_ID" 형식의 문자열입니다. ID, NAME, PARENT_ID는 하나의 공백으로 구분되어 있습니다.
# ID는 인형의 고유 번호를 나타내는 자연수입니다.
# 1 ≤ ID ≤ data의 길이
# data의 ID는 1부터 순차적으로 1씩 증가합니다.
# NAME은 인형 이름 혹은 특징을 나타내는 문자열입니다.
# 1 ≤ NAME의 길이 ≤ 20
# NAME은 다른 노드와 중복될 수 있습니다.
# NAME은 알파벳 대문자와 -(hyphen)로 이루어져 있습니다.
# PARENT_ID는 부모 노드의 ID를 나타내는 정수입니다.
# PARENT_ID는 0 이거나 ID 중 하나입니다.
# PARENT_ID가 0 이면 부모 노드가 없다는 뜻입니다.
# 1 ≤ word의 길이 ≤ 10
# word는 알파벳 대문자로 이루어진 문자열입니다.
# 입출력 예
#
# data	word	result
# ["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"]	"BROWN"	["CONY/DOLL/BROWN-CONY", "BROWN/DOLL/LARGE-BROWN", "BROWN/DOLL/SMALL-BROWN"]
# ["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"]	"SALLY"	["Your search for (SALLY) didn't return any results"]
# ["1 ROOTA 0", "2 AA 1", "3 ZZZ 1", "4 AABAA 1", "5 AAAAA 1", "6 AAAA 1", "7 BAAAAAAA 1", "8 BBAA 1", "9 CAA 1", "10 ROOTB 0", "11 AA 10"]	"AA"	["ROOTA/AA", "ROOTB/AA", "ROOTA/BAAAAAAA", "ROOTA/AAAAA", "ROOTA/AAAA", "ROOTA/AABAA", "ROOTA/CAA", "ROOTA/BBAA"]
# 입출력 예 설명
#
# 입출력 예 #1
#
# 2.jpg
#
# 리프 노드 중 NAME에 BROWN이 포함된 데이터는
#
# [
#     "5 LARGE-BROWN 3",
#     "6 SMALL-BROWN 3",
#     "8 BROWN-CONY 4"
# ]
# 입니다. (ID가 1인 데이터의 NAME이 BROWN이지만 인형 이름(리프 노드)이 아니므로 검색 대상이 아닙니다.)
#
# 3개의 데이터 중 NAME이 정확히 BROWN인 데이터는 없으므로 검색 조건 1에 의해 검색 순위가 결정되지 않습니다.
# 3개의 데이터 모두 BROWN을 한 번씩 포함하고 있어서 검색 조건 2에 의해 검색 순위가 결정되지 않습니다.
# 검색 조건 2-1에 의해 BROWN이 가장 앞에 위치해 있는 "BROWN-CONY"은 가장 먼저 검색되어야 합니다.
# 검색 조건 3에 의해 ID가 더 작은 "LARGE-BROWN"이 "SMALL-BROWN"보다 먼저 검색되어야 합니다.
# 즉, "BROWN-CONY", "LARGE-BROWN", "SMALL-BROWN" 순으로 검색되어야 합니다.
# 따라서 검색 결과는 인형의 특징(조상 노드)을 포함한 ["CONY/DOLL/BROWN-CONY", "BROWN/DOLL/LARGE-BROWN", "BROWN/DOLL/SMALL-BROWN"] 이어야 합니다.
#
# 입출력 예 #2
#
# 리프 노드 중 NAME에 SALLY가 포함된 데이터는 없습니다.
# 따라서 검색 결과는 ["Your search for (SALLY) didn't return any results"]이어야 합니다.
#
# 입출력 예 #3
#
# 3.jpg
#
# 리프 노드 중 NAME에 AA가 포함된 데이터는
#
# [
#     "2 AA 1",
#     "4 AABAA 1",
#     "5 AAAAA 1",
#     "6 AAAA 1",
#     "7 BAAAAAAA 1",
#     "8 BBAA 1",
#     "9 CAA 1",
#     "11 AA 10"
# ]
# 입니다.
#
# 검색 조건 1에 의하여 ID가 2, 11인 노드는NAME이 word와 정확히 일치하므로 가장 먼저 검색되어야 합니다.
# 검색 조건 2에 의하여 AA를 3번 포함한 "BAAAAAAA"가 3번째로 검색되어야 합니다. 또한, AA를 2번 포함한 "AABAA", "AAAA", "AAAAA"은 AA를 1번 포함한 "BBAA", "CAA"보다 먼저 검색되어야 합니다.
# 검색 조건 2-1에 의하여 "CAA"는 "BBAA"보다 먼저 검색되어야 합니다.
# 검색 조건 2-2에 의하여 AA가 보다 앞에 위치해 있는 "AAAA"와 "AAAAA"는 "AABAA"보다 먼저 검색되어야 합니다.
# 검색 조건 3에 의하여 ID가 2인 "AA"가 1번째로 검색되어야 하고 ID가 11인 "AA"가 2번째로 검색되어야 합니다. 또한, ID가 5인 "AAAAA"는 ID가 6인 "AAAA"보다 먼저 검색되어야 합니다.
# 즉, "AA", "AA", "BAAAAAAA", "AAAAA", "AAAA", "AABAA", "CAA", "BBAA"순으로 검색되어야 합니다.
# 따라서 검색 결과는 인형의 특징(조상 노드)을 포함한 ["ROOTA/AA", "ROOTB/AA", "ROOTA/BAAAAAAA", "ROOTA/AAAAA", "ROOTA/AAAA", "ROOTA/AABAA", "ROOTA/CAA", "ROOTA/BBAA"]이어야 합니다.
#
# 자식이 없는 노드 ↩
#
# 임의의 노드에서 루트 노드에 이르는 경로상에 있는 노드들 ↩

