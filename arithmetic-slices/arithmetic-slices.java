class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        if (nums.length < 3) return 0;

        int result = 0;
        int[] arr = new int[nums.length];
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] - nums[i-1] == nums[i-1] - nums[i-2]) {
                arr[i] = arr[i-1] + 1;
                result += arr[i];
            }
        }
        return result;
    }
}