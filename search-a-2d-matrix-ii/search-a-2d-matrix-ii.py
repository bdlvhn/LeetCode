class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        i, j = 0, n
        while (0 <= i <= m) and (0 <= j <= n):
            if matrix[i][j] == target:
                return True

            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
        return False