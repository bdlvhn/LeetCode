import collections

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor: return image

        queue = collections.deque()
        queue.append((sr, sc))

        dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
        while queue:
            x, y = queue.popleft()
            if image[x][y] != oldColor: continue
            image[x][y] = newColor
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (0 <= nx < len(image)) and (0 <= ny < len(image[0])):
                    queue.append((nx, ny))
        return image