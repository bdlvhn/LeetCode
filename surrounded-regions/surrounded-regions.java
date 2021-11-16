class Solution {
    public void solve(char[][] board) {
        int m = board.length, n = board[0].length;
        for (int i = 0; i < m; i++) {
            if (i == 0 || i == m - 1) {
                for (int j = 0; j < n; j++) {
                    if (board[i][j] == 'O') change(i, j, board);
                }
            } else {
                if (board[i][0] == 'O') change(i, 0, board);
                if (board[i][n - 1] == 'O') change(i, n-1, board);
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '*') board[i][j] = 'O';
            }
        }
    }

    private void change(int x, int y, char[][] board) {
        if (x >= 0 && x < board.length && y >= 0 && y < board[0].length &&
                board[x][y] == 'O') {
            board[x][y] = '*';
            change(x + 1, y, board);
            change(x - 1, y, board);
            change(x, y + 1, board);
            change(x, y - 1, board);

        }
    }
}