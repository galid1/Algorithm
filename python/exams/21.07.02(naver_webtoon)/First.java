package com.galid.java_test.webtoon;

import java.math.BigDecimal;
import java.util.Arrays;
import java.util.Collections;

public class First {
    public static void main(String[] args) {
        Solution s = new Solution();
//        int[] prices =  new int[]{32000, 18000, 42500};
//        int[] discounts = new int[]{ 50, 20, 65 };
        int[] prices =  new int[]{13000, 88000, 10000};
        int[] discounts = new int[]{30, 20};
        s.solution(prices, discounts);
    }
}


class Solution {
    public int solution(int[] prices, int[] discounts) {
        int[] orderedPrices = Arrays.stream(Arrays.stream(prices).boxed().toArray(Integer[]::new))
                .sorted(Collections.reverseOrder())
                .mapToInt(Integer::intValue)
                .toArray();
        int[] orderedDiscounts = Arrays.stream(Arrays.stream(discounts).boxed().toArray(Integer[]::new))
                .sorted(Collections.reverseOrder())
                .mapToInt(Integer::intValue)
                .toArray();


        int answer = 0;

        int curPriceIdx = 0;
        for (int i = 0; i < orderedDiscounts.length; i++) {
            int subDiscount = 100 - orderedDiscounts[i];
            answer += BigDecimal
                    .valueOf(
                            orderedPrices[curPriceIdx])
                                .multiply(BigDecimal.valueOf(subDiscount/100.0)
                    )
                    .intValue();
            curPriceIdx ++;
        }

        while (curPriceIdx < prices.length) {
            answer += orderedPrices[curPriceIdx++];
        }

        return answer;
    }
}