class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.findArea(grid, i, j))

        return maxArea

    def findArea(self, board: List[List[int]], i: int, j: int) -> int:
        queue = collections.deque()
        queue.append((i, j))

        area = 0
        dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
        while queue:
            x, y = queue.popleft()
            if board[x][y] != 1: continue
            board[x][y] = 0
            area += 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (0 <= nx < len(board)) and (0 <= ny < len(board[0])):
                    queue.append((nx, ny))
        return area