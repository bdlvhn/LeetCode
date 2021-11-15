class Solution {
    public int findCircleNum(int[][] isConnected) {
        int count = 0;
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < isConnected.length; i++) {
            for (int j = 0; j < isConnected[0].length; j++) {
                if (i != j && isConnected[i][j] == 1) queue.add(new int[]{i, j});
            }
            if (isConnected[i][i] == 1) {
                count++;
                while (!queue.isEmpty()) {
                    int[] poll = queue.poll();
                    int x = poll[0], y = poll[1];
                    if (isConnected[x][y] == 1) {
                        isConnected[y][y] = 0;
                        isConnected[x][y] = 0;
                        isConnected[y][x] = 0;
                        for (int k = 0; k < isConnected.length; k++) {
                            if(y != k && isConnected[y][k] == 1) {
                                queue.add(new int[]{y, k});
                            }
                        }
                    }
                }
            }
        }
        return count;
    }
}