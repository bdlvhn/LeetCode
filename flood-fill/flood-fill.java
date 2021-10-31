class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int oldColor = image[sr][sc];
        if (oldColor == newColor) return image;
        dfs(image, sr, sc, oldColor, newColor);
        return image;
    }

    int[] dx = {1, 0, -1, 0}, dy = {0, -1, 0, 1};
    private void dfs(int[][] board, int x, int y, int oldColor, int newColor) {
        if (board[x][y] != oldColor) {
            return;
        }

        board[x][y] = newColor;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if ((0 <= nx) & (nx < board.length) & (0 <= ny) & ( ny < board[0].length)) {
                dfs(board, nx, ny, oldColor, newColor);
            }
        }
    }
}