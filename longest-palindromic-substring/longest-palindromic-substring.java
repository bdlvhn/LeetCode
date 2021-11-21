class Solution {
    int low, maxLen;
    // 5. Longest Palindromic Substring
    public String longestPalindrome(String s) {
        if (s.length() == 1) return s;

        for (int i = 0; i < s.length(); i++) {
            findPalindrome(s, i, i);
            findPalindrome(s, i, i+1);
        }
        return s.substring(low, low + maxLen);
    }

    private void findPalindrome(String s, int left, int right) {
        while (left >= 0 && right < s.length() && (s.charAt(left) == s.charAt(right))) {
            left--;
            right++;
        }
        
        if (maxLen < right - left - 1) {
            low = left + 1;
            maxLen = right - left - 1;
        }
    }
}