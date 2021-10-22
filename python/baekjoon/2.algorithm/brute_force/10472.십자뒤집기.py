# JAVA
# import java.io.BufferedReader;
# import java.io.IOException;
# import java.io.InputStreamReader;
# import java.util.*;
#
# public class Main {
#     public static class Board implements Cloneable {
#         char[] board;
#
#         public Board(char[] board) {
#             this.board = board;
#         }
#
#         @Override
#         protected Board clone() throws CloneNotSupportedException {
#             return new Board(this.board.clone());
#         }
#     }
#
#     public static int[] ds = new int[]{0, -1, 1, 3, -3};
#
#     public static int solve(String dest) throws CloneNotSupportedException {
#         Board init = new Board(new char[]{'.', '.', '.', '.', '.', '.', '.', '.', '.'});
#
#         Queue<Board> q = new LinkedList<>();
#         q.offer(init);
#
#         Set<String> visited = new HashSet<>();
#
#         int ans = 0;
#         while (!q.isEmpty()) {
#             int curSize = q.size();
#             for (int i = 0; i < curSize; i++) {
#                 Board curBoard = q.poll();
#
#                 if (isEnd(curBoard, dest)) {
#                     return ans;
#                 }
#
#                 for (int j = 0; j < 9; j++) {
#                     Board nextBoard = curBoard.clone();
#                     reverse(j, nextBoard);
#
#                     String sBoard = boardToString(nextBoard);
#                     if (visited.contains(sBoard)) continue;
#
#                     visited.add(sBoard);
#                     q.add(nextBoard);
#                 }
#             }
#
#             ans += 1;
#         }
#
#         return ans;
#     }
#
#     public static void reverse(int j, Board board) {
#         for (int d : ds) {
#             int target = j + d;
#
#             if (target < 0) continue;
#             if (target >= 9) continue;
#
#             if (d == -1 || d == 1) {
#                 int curRow = j/3;
#                 int targetRow = target/3;
#
#                 if (curRow != targetRow) continue;
#             }
#
#             if (board.board[target] == '.') {
#                 board.board[target] = '*';
#             }
#             else {
#                 board.board[target] = '.';
#             }
#         }
#     }
#
#     public static boolean isEnd(Board curBoard, String dest) {
#         return boardToString(curBoard).equals(dest);
#     }
#
#     public static String boardToString(Board board) {
#         return String.valueOf(board.board);
#     }
#
#     public static void main(String[] args) throws IOException, CloneNotSupportedException {
#         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
#         int t = Integer.parseInt(br.readLine());
#
#         for (int r = 0; r < t; r++) {
#             StringBuilder sb = new StringBuilder();
#             for (int i = 0; i < 3; i++) {
#                 sb.append(br.readLine());
#             }
#
#             System.out.println(solve(sb.toString()));
#         }
#     }
# }

import sys, copy
from collections import deque


def solve():
    global dest_board, dest_bin_board

    visited = [False for _ in range(1000)]
    init_board = [['.' for _ in range(3)] for _ in range(3)]
    visited[convert_bin(init_board)] = True
    q = deque([init_board])

    if convert_bin(init_board) == dest_bin_board:
        return print(0)

    ans = 0
    while q:
        ans += 1
        for _ in range(len(q)):
            c_board = q.popleft()

            for i in range(3):
                for j in range(3):
                    next_board = copy.deepcopy(c_board)
                    reverse(i, j, next_board)

                    bin_board = convert_bin(next_board)

                    if visited[bin_board]:
                        continue

                    if clear(bin_board):
                        return print(ans)

                    visited[bin_board] = True
                    q.append(next_board)


def convert_bin(board):
    bin_board = ''
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                bin_board += '0'
            else:
                bin_board += '1'

    return int(bin_board, 2)


def clear(bin_board):
    global dest_bin_board

    return bin_board == dest_bin_board


def reverse(i, j, board):
    global ds
    for di in range(5):
        ni, nj = i + ds[di][0], j + ds[di][1]
        if 0 <= ni < 3 and 0 <= nj < 3:
            board[ni][nj] = '*' if board[ni][nj] == '.' else '.'


ds = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
t = int(sys.stdin.readline().strip())
for _ in range(t):
    dest_board = []
    for _ in range(3):
        dest_board.append(list(sys.stdin.readline().strip()))
    dest_bin_board = convert_bin(dest_board)

    solve()