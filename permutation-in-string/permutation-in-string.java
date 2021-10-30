class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int len1 = s1.length();
        int len2 = s2.length();
        if (len1 > len2) {
            return false;
        }

        int[] dict = new int[26];
        for (int i = 0; i < len1; i++) {
            dict[s1.charAt(i) - 'a']++;
            dict[s2.charAt(i) - 'a']--;
        }

        if (allZero(dict)) return true;

        for (int j = len1; j < len2; j++) {
            dict[s2.charAt(j) - 'a']--;
            dict[s2.charAt(j - len1) - 'a']++;
            if (allZero(dict)) return true;
        }
        return false;
    }

    private boolean allZero(int[] dict) {
        for (int i = 0; i < 26; i++) {
            if (dict[i] != 0) {
                return false;
            }
        }
        return true;
    }
}