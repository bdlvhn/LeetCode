class Solution {
    public int[] searchRange(int[] nums, int target) {
        if (nums.length == 0) return new int[]{-1, -1};
        int[] result = new int[]{(int)(Math.pow(10,5)) + 1, -1};

        doSearch(nums, target, result, 0, nums.length-1);
        return result[0] == (int)(Math.pow(10,5)) + 1 & result[1] == -1 ? new int[]{-1, -1} : result;
    }

    private void doSearch(int[] nums, int target, int[] result, int left, int right) {
        if (left > right) return;

        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            result[0] = Math.min(result[0], mid);
            result[1] = Math.max(result[1], mid);
            doSearch(nums, target, result, left, mid - 1);
            doSearch(nums, target, result, mid + 1, right);
        } else if (nums[mid] < target) {
            doSearch(nums, target, result, mid + 1, right);
        } else {
            doSearch(nums, target, result, left, mid - 1);
        }
    }
}