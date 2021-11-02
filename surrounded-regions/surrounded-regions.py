class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        queue = collections.deque()
        
        for i in range(m):
            if board[i][0] == 'O': queue.append((i,0))
            if board[i][n-1] == 'O': queue.append((i,n-1))

        for j in range(n):
            if board[0][j] == 'O': queue.append((0, j))
            if board[m-1][j] == 'O': queue.append((m-1, j))
        
        dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
        while queue:
            x, y = queue.popleft()
            board[x][y] = '+'
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if (0 <= nx < m) and (0 <= ny < n) and board[nx][ny] == 'O':
                    queue.append((nx, ny))
        
        for a in range(m):
            for b in range(n):
                if board[a][b] == 'O': board[a][b] = 'X'
                if board[a][b] == '+': board[a][b] = 'O'