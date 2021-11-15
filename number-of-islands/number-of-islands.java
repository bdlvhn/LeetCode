class Solution {
    public int numIslands(char[][] grid) {
        int result = 0;
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    result++;
                    queue.add(new int[]{i, j});
                    while (!queue.isEmpty()) {
                        int[] poll = queue.poll();
                        int x = poll[0], y = poll[1];
                        if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length && grid[x][y] == '1') {
                            grid[x][y] = '0';
                            queue.add(new int[]{x+1, y});
                            queue.add(new int[]{x, y+1});
                            queue.add(new int[]{x-1, y});
                            queue.add(new int[]{x, y-1});
                        }
                    }
                }
            }
        }
        return result;
    }
}