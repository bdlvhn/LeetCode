class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])

        def dfs(x: int, y: int, route: List = []) -> List:
            if grid[x][y] == "0":
                return route

            route.append([x, y])
            grid[x][y] = "0"

            dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
            for n in range(4):
                nx, ny = x + dx[n], y + dy[n]
                if 0 <= nx < row and 0 <= ny < col and ([nx, ny]) not in route:
                    route = dfs(nx, ny, route)
            return route
        answer = 0

        for i in range(row):
            for j in range(col):
                answer += len(dfs(i, j, [])) > 0
        return answer