class Solution {
    public int orangesRotting(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int fresh = 0, second = 0;
        LinkedList<int[]> rotten = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) fresh++;
                if (grid[i][j] == 2) rotten.add(new int[]{i, j});
            }
        }
        if (fresh == 0 && rotten.isEmpty()) return 0;

        int[] dx = {0, -1, 0, 1}, dy = {1, 0, -1, 0};
        while (!rotten.isEmpty()) {
            int size = rotten.size();
            for (int i = 0; i < size; i++) {
                int[] temp = rotten.poll();
                for (int j = 0; j < 4; j++) {
                    int nx = temp[0] + dx[j], ny = temp[1] + dy[j];
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1) {
                        grid[nx][ny] = 2;
                        rotten.add(new int[]{nx, ny});
                        fresh--;
                    }
                }
            }
            second++;
        }

        if (fresh != 0) return -1;
        return second - 1;
    }
}