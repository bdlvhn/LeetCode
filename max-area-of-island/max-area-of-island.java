class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int maxArea = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    maxArea = Math.max(maxArea, findIsland(grid, i, j));
                }
            }
        }
        return maxArea;
    }

    private int findIsland(int[][] board, int i, int j) {
        ArrayDeque<Object> queue = new ArrayDeque<>();
        queue.addFirst(new int[]{i, j});
        int area = 0;

        int[] dx = {1, 0, -1, 0}, dy = {0, -1, 0, 1};
        while (!queue.isEmpty()) {
            int[] temp = (int[]) queue.pollFirst();
            int x = temp[0], y = temp[1];
            if (board[x][y] != 1) continue;
            board[x][y] = 0;
            area++;
            
            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k], ny = y + dy[k];
                if ((0 <= nx) & (nx < board.length) & (0 <= ny) & (ny < board[0].length)) {
                    queue.addLast(new int[]{nx, ny});
                }
            }
        }
        return area;
    }
}