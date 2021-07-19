class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x: int, y: int, area: int) -> int:
            if grid[x][y] == 0:
                return area

            grid[x][y] = 0
            area += 1
            dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    area = dfs(nx, ny, area)
            return area

        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    answer = max(answer, dfs(i, j, 0))
        return answer