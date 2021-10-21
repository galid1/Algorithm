# JAVA
# package com.example.java_study;
#
# import java.io.BufferedReader;
# import java.io.IOException;
# import java.io.InputStreamReader;
# import java.util.*;
#
# public class Main {
# //    5 2
# //    4 1 2 3 5
#
#     public static void solve(int n, int k, int nums[]) {
#         OptionalInt first = Arrays.stream(nums)
#                 .sorted()
#                 .skip(k - 1)
#                 .findFirst();
#
#         System.out.println(first.getAsInt());
#     }
#
#     public static void main(String[] args) throws IOException {
#         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
#         StringTokenizer st = new StringTokenizer(br.readLine());
#
#         int n = Integer.parseInt(st.nextToken());
#         int k = Integer.parseInt(st.nextToken());
#
#         int[] nums = new int[n];
#         st = new StringTokenizer(br.readLine());
#         for (int i = 0; i < n; i++) {
#             nums[i] = Integer.parseInt(st.nextToken());
#         }
#
#         solve(n, k, nums);
#     }
# }


import sys


def solve():
    global n, k, nums

    nums.sort()
    print(nums[k-1])


n, k = map(int, sys.stdin.readline().strip().split(" "))
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()