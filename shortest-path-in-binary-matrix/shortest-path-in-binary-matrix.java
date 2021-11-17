class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 | grid[n-1][n-1] == 1) return -1;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0});
        int[][] visited = new int[n][n];
        visited[0][0] = 1;

        int[] dx = {1, 1, 1, 0, 0, -1, -1, -1}, dy = {1, 0, -1, 1, -1, 1, 0, -1};
        while (!queue.isEmpty()) {
            int[] poll = queue.poll();
            int x = poll[0], y = poll[1];
            if (x == n-1 && y == n-1) {
                return visited[x][y];
            }
            for (int i = 0; i < 8; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (isValid(nx, ny, grid, visited)) {
                    queue.add(new int[]{nx, ny});
                    visited[nx][ny] = visited[x][y] + 1;
                }
            }
        }
        return -1;
    }

    private boolean isValid(int nx, int ny, int[][] grid, int[][] visited) {
        return (nx >= 0 && nx < grid.length && ny >= 0 && ny < grid.length && grid[nx][ny] == 0 && visited[nx][ny] == 0);
    }
}