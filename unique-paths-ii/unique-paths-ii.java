class Solution {
    public int uniquePathsWithObstacles(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] obstacles = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    obstacles[i][j] = 1;
                    grid[i][j] = 0;
                }
            }
        }

        grid[0][0] = obstacles[0][0] == 1 ? 0 : 1;
        for (int i = 1; i < m; i++) grid[i][0] = obstacles[i][0] == 1 || grid[i - 1][0] == 0 ? 0 : 1;
        for (int j = 1; j < n; j++) grid[0][j] = obstacles[0][j] == 1 || grid[0][j - 1] == 0 ? 0 : 1;

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                grid[i][j] = obstacles[i][j] == 1 ? 0 : grid[i - 1][j] + grid[i][j - 1];
            }
        }
        return grid[m - 1][n - 1];
    }
    
    
    
}
    