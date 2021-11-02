class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int[][] visited = new int[m][n];
        Queue<int[]> queue = new LinkedList<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    visited[i][j] = 1;
                    queue.add(new int[]{i, j});
                }
            }
        }

        int[] dx = {0, 1, 0, -1}, dy = {1, 0, -1, 0};
        while (!queue.isEmpty()) {
            int[] temp = queue.poll();
            int x = temp[0], y = temp[1];
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && visited[nx][ny] == 0) {
                    mat[nx][ny] = visited[x][y];
                    visited[nx][ny] = visited[x][y] + 1;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
        return mat;
    }
}