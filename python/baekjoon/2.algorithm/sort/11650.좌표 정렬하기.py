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
#     public static int n;
#     public static int[][] cs;
#
#     public static void solve() {
#         Arrays.stream(cs)
#                 .sorted((c1, c2) -> {
#                     if (c1[0] <= c2[0]) {
#                         if (c1[0] == c2[0]) {
#                             return c1[1] - c2[1];
#                         }
#                         return -1;
#                     } else {
#                         return 1;
#                     }
#                 })
#                 .forEach(coords -> {
#                     System.out.println(coords[0] + " " + coords[1]);
#                 });
#
#
#     }
#
#     public static void main(String[] args) throws IOException {
#         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
#         StringTokenizer st = null;
#
#         n = Integer.parseInt(br.readLine());
#         cs = new int[n][2];
#
#         for(int i = 0; i < n; i++) {
#             st = new StringTokenizer(br.readLine());
#             cs[i][0] = Integer.parseInt(st.nextToken());
#             cs[i][1] = Integer.parseInt(st.nextToken());
#         }
#
#         solve();
#
# //        5
# //        3 4
# //        1 1
# //        1 -1
# //        2 2
# //        3 3
#     }
# }

import sys


def solve():
    global n, cs

    cs.sort(key=lambda item: (item[0], item[1]))

    for x, y in cs:
        print(x, y)


n = int(sys.stdin.readline().strip())
cs = []
for _ in range(n):
    cs.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve()