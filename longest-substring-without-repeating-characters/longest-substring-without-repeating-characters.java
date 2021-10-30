class Solution {
    public int lengthOfLongestSubstring(String s) {

        int len = s.length();
        if (len <= 1) {
            return len;
        }

        HashMap<Character, Integer> map = new HashMap<>();
        int start = 0;
        int maxLen = 0;

        for (int end = 0; end < len; end++) {
            char now = s.charAt(end);
            if (map.containsKey(now)) {
                start = Math.max(start, map.get(now) + 1);
            }
            map.put(now, end);
            maxLen = Math.max(maxLen, end - start + 1);
        }

        return maxLen;
    }
}