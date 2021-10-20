import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class Main {
   public static void solve(int n, int[][] infos) {
       int ans = 0;
       boolean[] visited = new boolean[n];

       for (int i = 0; i < n; i ++) {
           if(visited[i]) continue;

           ans ++;
           visited[i] = true;

           for (int j = i+1; j < n; j++) {
               if (linked(i, j, infos)) {
                   dfs(n, j, infos, visited);
               }
           }
       }

       System.out.println(ans);
   }

   public static void dfs(int n, int i, int[][] infos, boolean[] visited) {
       for(int j = 0; j < n; j ++) {
           if(visited[j]) continue;

           if (linked(i, j, infos)) {
               visited[j] = true;
               dfs(n, j, infos, visited);
           }
       }
   }

    public static boolean linked(int i, int j, int[][] infos) {
        int xi = infos[i][0];
        int yi = infos[i][1];
        int ri = infos[i][2];

        int xj = infos[j][0];
        int yj = infos[j][1];
        int rj = infos[j][2];

        double dis = Math.sqrt(Math.abs(Math.pow(xi - xj, 2)) + Math.abs(Math.pow(yi - yj, 2)));

        return ri + rj >= dis;
    }

    public static void main(String[] args) throws IOException {
        InputStreamReader is = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(is);

        StringTokenizer st = new StringTokenizer(br.readLine());

        int t = Integer.parseInt(st.nextToken());

        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int[][] infos = new int[n][3];

            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                int idx = 0;
                while (st.hasMoreTokens()) {
                    infos[j][idx] = Integer.parseInt(st.nextToken());
                    idx += 1;
                }
            }

            solve(n, infos);
        }

        br.close();
        is.close();
    }
}