# JAVA
# package com.example.java_study;
#
# import java.io.BufferedReader;
# import java.io.IOException;
# import java.io.InputStreamReader;
# import java.util.*;
#
# public class Main {
#
#     public static void solve(int n, int[] nums, int x) {
#         nums = Arrays.stream(nums).sorted().toArray();
#
#         int ans = 0;
#         int i = 0;
#         int j = n-1;
#
#         while (i < j) {
#             int cur_sum = nums[i] + nums[j];
#
#             if (cur_sum > x) {
#                 j -= 1;
#             }
#             else if(cur_sum < x) {
#                 i += 1;
#             }
#             else {
#                 ans += 1;
#                 i += 1;
#                 j -= 1;
#             }
#         }
#
#         System.out.println(ans);
#     }
#
#     public static void main(String[] args) throws IOException {
#         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
#         StringTokenizer st;
#
#         int n = Integer.parseInt(br.readLine());
#         int[] nums = new int[n];
#
#         st = new StringTokenizer(br.readLine());
#         for(int i = 0; i < n; i ++) {
#             nums[i] = Integer.parseInt(st.nextToken());
#         }
#
#         int x = Integer.parseInt(br.readLine());
#
#         solve(n, nums, x);
#     }
# }


import sys


def solve():
    global n, nums, x

    nums.sort()

    i, j = 0, n - 1
    ans = 0

    while i < j:
        cur_sum = nums[i] + nums[j]

        if cur_sum > x:
            j -= 1

        elif cur_sum < x:
            i += 1

        else:
            ans += 1
            i += 1
            j -= 1

    print(ans)


n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
x = int(sys.stdin.readline().strip())

solve()
