class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, wall = 0, len(matrix[0])
        while x < len(matrix):
            idx = bisect.bisect_right(matrix[x],target,0,wall)

            if matrix[x][idx-1] == target:
                return True
            else:
                x += 1
                wall = idx
        return False