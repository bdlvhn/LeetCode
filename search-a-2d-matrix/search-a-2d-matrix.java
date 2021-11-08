class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length - 1, n = matrix[0].length - 1;
        int col = binarySearchRow(matrix, target, 0, m);
        return binarySearchCol(matrix, target, col, 0, n);
    }

    private boolean binarySearchCol(int[][] matrix, int target, int row, int low, int high) {
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (matrix[row][mid] == target) {
                return true;
            } else if (matrix[row][mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return false;
    }

    private int binarySearchRow(int[][] matrix, int target, int low, int high) {
        int n = matrix[0].length - 1;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (matrix[mid][n] == target) {
                return mid;
            } else if (matrix[mid][n] < target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
}