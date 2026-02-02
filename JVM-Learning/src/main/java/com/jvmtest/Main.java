package com.jvmtest;
import java.util.Arrays;
import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // 注意 hasNext 和 hasNextLine 的区别
        int[] a = new int[n];
        int[] b = new int[n];
        for(int i = 0; i < n; i++){
            a[i] = in.nextInt();
        }
        for(int i = 0; i < n; i++){
            b[i] = in.nextInt();
        }

        int gap = 0;
        for(int i = 0; i < n; i++){
            gap += Math.abs(a[i] - b[i]);
        }
        if(gap % 2 == 1){
            System.out.println(-1);
        } else {
            System.out.println(gap / 2);
        }
    }


    public static void test(){
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        int n = in.nextInt(), m = in.nextInt(), k = in.nextInt();
        int[][] matrix = new int[n][m];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                matrix[i][j] = in.nextInt();
            }
        }

        int[][][][] dp = new int[n][m][n][m];
        int x1 = in.nextInt()-1, y1 = in.nextInt()-1, x2 = in.nextInt()-1, y2 = in.nextInt()-1;
        int Ex = in.nextInt()-1, Ey = in.nextInt()-1;
        System.out.println(color(dp, matrix, x1, y1, Ex, Ey, n, m, k));
        System.out.println(color(dp, matrix, x2, y2, Ex, Ey, n, m, k));
    }

    public static int color(int[][][][] dp, int[][] matrix, int x, int y, int dx, int dy, int n, int m, int k){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                dp[x][y][i][j] = -1;
            }
        }
        dp[x][y][x][y] = 0;
        dfs(dp, matrix, x, y, n, m, k);

        return dp[x][y][dx][dy];
    }

    public static void dfs(int[][][][] dp, int[][] matrix, int x, int y, int n, int m, int k){
        int left = x-1, right = x+1, top = y-1, bottom = y+1;
        if(left >= 0){
            if(dp[x][y][left][y] == -1){
                dp[x][y][left][y] = Math.abs(matrix[x][y]-matrix[left][y]) <= k ? dp[x][y][x][y] : dp[x][y][x][y]+6;
            }
        }
        if(right <= m){
            if(dp[x][y][right][y] == -1){
                dp[x][y][right][y] = Math.abs(matrix[x][y]-matrix[right][y]) <= k ? dp[x][y][x][y] : dp[x][y][x][y]+6;
            }
        }
        if(top >= 0){
            if(dp[x][y][x][top] == -1){
                dp[x][y][x][top] = Math.abs(matrix[x][y]-matrix[x][top]) <= k ? dp[x][y][x][y] : dp[x][y][x][y]+6;
            }
        }
        if(bottom <= n){
            if(dp[x][y][x][bottom] == -1){
                dp[x][y][x][bottom] = Math.abs(matrix[x][y]-matrix[x][bottom]) <= k ? dp[x][y][x][y] : dp[x][y][x][y]+6;
            }
        }
        dfs(dp, matrix, left, y, n, m, k);
        dfs(dp, matrix, right, y, n, m, k);
        dfs(dp, matrix, x, top, n, m, k);
        dfs(dp, matrix, x, bottom, n, m, k);
    }
}
