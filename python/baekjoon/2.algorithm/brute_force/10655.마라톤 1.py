# JAVA
# import java.io.BufferedReader;
# import java.io.IOException;
# import java.io.InputStreamReader;
# import java.util.*;
#
# public class Main {
#     public static int totalDistance;
#     public static int[][] cs;
#
#     public static void solve(int n, int[][] cs) {
#         int minDistance = totalDistance;
#
#         for(int i = 1; i < n-1; i ++) {
#             int tempTotalDistance = totalDistance;
#
#             tempTotalDistance -= (calDistance(i-1, i) + calDistance(i, i+1));
#             tempTotalDistance += calDistance(i-1, i+1);
#
#             minDistance = Math.min(minDistance, tempTotalDistance);
#         }
#
#         System.out.println(minDistance);
#     }
#
#     public static int calDistance(int i, int j) {
#         return Math.abs(cs[i][0] - cs[j][0]) + Math.abs(cs[i][1] - cs[j][1]);
#     }
#
#     public static void main(String[] args) throws IOException {
#         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
#         int n = Integer.parseInt(br.readLine());
#
#         cs = new int[n][2];
#         for (int i = 0; i < n; i++) {
#             StringTokenizer st = new StringTokenizer(br.readLine());
#             cs[i][0] = Integer.parseInt(st.nextToken());
#             cs[i][1] = Integer.parseInt(st.nextToken());
#
#             if (i >= 1) {
#                 totalDistance += calDistance(i, i-1);
#             }
#         }
#
#         solve(n, cs);
#     }
# }

import sys


def solve():
    global n, cs, td

    min_td = td

    for i in range(1, n-1):
        t_td = td
        t_td -= (cal_d(i-1, i) + cal_d(i, i+1))
        t_td += cal_d(i-1, i+1)

        min_td = min(min_td, t_td)

    print(min_td)


def cal_d(i, j):
    global cs

    return abs(cs[i][0] - cs[j][0]) + abs(cs[i][1] - cs[j][1])



n = int(sys.stdin.readline().strip())
cs = []
td= 0
for i in range(n):
    cs.append(list(map(int, sys.stdin.readline().strip().split(" "))))

    d = cal_d(i-1, i)
    td += d

solve()