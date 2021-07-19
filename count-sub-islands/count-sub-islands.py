class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])

        def dfs(x: int, y: int, isSub: bool) -> int:
            if grid2[x][y] == 0:
                return isSub

            grid2[x][y] = 0
            if grid1[x][y] == 0:
                isSub = False

            dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    isSub = (dfs(nx, ny, isSub) and isSub)
            return isSub

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    count += dfs(i, j, True)
        return count