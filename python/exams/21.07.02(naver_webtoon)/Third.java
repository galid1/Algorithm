package com.galid.java_test.webtoon;


import java.util.Arrays;
import java.util.LinkedList;
import java.util.stream.Collectors;

import static java.lang.Integer.max;

public class Third {
    public static void main(String[] args) {
        String s = "aabcbcd";
        String t = "abc";

        Solution3 s3 = new Solution3();
        s3.solution3(s, t);
    }
}

class Solution3 {
    public int solution3(String s, String t) {
        int result = 0;
        String[] splitT = t.split("");

        int startIdx = 0;
        LinkedList<String> splitS = Arrays.stream(s.split(""))
                .collect(Collectors.toCollection(LinkedList::new));

        int sSize = splitS.size();
        while (sSize > 0) {
            boolean changed = false;
            result ++;

            for (int i = 0;  i < sSize; i++) {
                // 같으면 제거
                if (isSame(splitS, startIdx, splitT)) {
                    for (int j = 0; j < t.length(); j++) {
                        splitS.remove(startIdx);
                    }

                    startIdx = max(0, startIdx-t.length());
                    changed = true;
                }
            }

            sSize = splitS.size();
            if (!changed) {
                break;
            }
        }
        return result;
    }

    public boolean isSame(LinkedList<String> splitS, int sIdx, String[] t) {
        for (int i = 0; i < t.length; i++) {
            if (!splitS.get(sIdx++).equals(t[i])) {
                return false;
            }
        }

        return true;
    }
}

