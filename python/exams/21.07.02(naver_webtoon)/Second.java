package com.galid.java_test.webtoon;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

public class Second {
    public static void main(String[] args) {
        Solution2 s = new Solution2();
        s.solution2("asdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfasasdfasdfas");

    }
}

class Solution2 {
    // abaabababa의 경우로 예로들어서
    // a b a ab ab a b a 이렇게 안나누고 아래처럼 나누는것 가능하지만 이게 더 많이 잘라짐 결국엔
    // aba ab ab aba  => 그리디하게 풀어도 됨

    public String[] solution2(String s) {
        List<String> answer = new ArrayList<>();

        LinkedList<String> splitS = Arrays.stream(s.split(""))
                .collect(Collectors.toCollection(LinkedList::new));

        LinkedList<String> rightWords = new LinkedList<>();

        while (true) {
            // 더이상 글자가 없음
            if (splitS.size() == 0) break;

            int midIdx = ((splitS.size() + 1) / 2);
            int leftIdx = 0;
            int rightIdx = splitS.size();
            String leftC = splitS.get(leftIdx);
            String rightC = "";

            // 같은 글자의 오른쪽 인덱스 찾기
            while (!leftC.equals(rightC)) {
                rightIdx -= 1;
                if (midIdx >= rightIdx) break;

                rightC = splitS.get(rightIdx);
            }

            // 해당 글자가 같은지 확인
            if (!isSame(splitS, leftIdx, rightIdx)) break;

            int wordSize = splitS.size() - rightIdx;

            StringBuilder leftWord = new StringBuilder();
            StringBuilder rightWord = new StringBuilder();
            for (int i = 0; i < wordSize; i++) {
                leftWord.append(splitS.poll());
                rightWord.insert(0, splitS.removeLast());
            }

            answer.add(leftWord.toString());
            rightWords.add(rightWord.toString());
        }

        // 마지막 단어 추가
        if (splitS.size() > 0) {
            StringBuilder sb = new StringBuilder();
            for (String c: splitS) {
                sb.append(c);
            }
            answer.add(sb.toString());
        }

        int rightWordListSize = rightWords.size();
        for (int j = 0; j < rightWordListSize; j++) {
            answer.add(rightWords.removeLast());
        }

        return answer.toArray(String[]::new);
    }

    public static boolean isSame(LinkedList<String> splitS, int lIdx, int rIdx) {
        while (rIdx < splitS.size()) {
            if (!splitS.get(lIdx).equals(splitS.get(rIdx)))
                return false;

            lIdx++;
            rIdx++;
        }
        return true;
    }
}