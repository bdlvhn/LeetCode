class Solution {
    public int findMin(int[] nums) {
        int low = 0;
        int high = nums.length-1;
        int mid;

        while (low < high) {
            mid = low + (high - low) / 2;
            if (nums[low] < nums[high]) {
                break;
            }
            else if (nums[mid] < nums[high]) {
                high = mid;
            }
            else {
                low = mid + 1;
            }
        }
        return nums[low];
    }
}