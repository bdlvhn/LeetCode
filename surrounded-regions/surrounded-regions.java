class Solution {
    static int m, n;
    
    public void solve(char[][] board) {
        m = board.length;
        n = board[0].length;
        Queue<int[]> queue = new LinkedList<>();

        findEdges(board, queue);
        bfs(board, queue);

        for (int x = 0; x < m; x++) {
            for (int y = 0; y < n; y++) {
                if (board[x][y] == 'O') board[x][y] = 'X';
                if (board[x][y] == '+') board[x][y] = 'O';
            }
        }
    }

    private void findEdges(char[][] board, Queue<int[]> queue) {
        for (int r = 0; r < m; r++) {
            if (board[r][0] == 'O') {
                board[r][0] = '+';
                queue.add(new int[]{r, 0});
            }

            if (board[r][n-1] == 'O') {
                board[r][n-1] = '+';
                queue.add(new int[]{r, n-1});
            }
        }

        for (int c = 0; c < n; c++) {
            if (board[0][c] == 'O') {
                board[0][c] = '+';
                queue.add(new int[]{0, c});
            }
            if (board[m-1][c] == 'O') {
                board[m-1][c] = '+';
                queue.add(new int[]{m-1, c});
            }
        }
    }

    private void bfs(char[][] board, Queue<int[]> queue) {
        int[] dx = {1, 0, -1, 0}, dy = {0, -1, 0, 1};
        while (!queue.isEmpty()) {
            int[] temp = queue.poll(); 
            int x = temp[0], y = temp[1];
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && board[nx][ny] == 'O') {
                    board[nx][ny] = '+';
                    queue.add(new int[]{nx, ny});
                }
            }
        }
    }
    
}