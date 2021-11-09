class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findRow(matrix, target)
        return self.findCol(matrix, row, target)


    def findRow(self, matrix: List[List[int]], target: int) -> int:
        low, high = 0, len(matrix) - 1
        while low < high:
            mid = int(low + (high - low) / 2)
            if (matrix[mid][len(matrix[0])-1] < target):
                low = mid + 1
            else:
                high = mid
        return low

    def findCol(self, matrix: List[List[int]], row: int, target: int) -> bool:
        low, high = 0, len(matrix[0]) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False