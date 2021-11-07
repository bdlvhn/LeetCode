class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n < 0) return false;
        String binInt = Integer.toBinaryString(n);
        long count = binInt.chars().filter(ch -> ch == '1').count();
        return count == 1;
    }
}