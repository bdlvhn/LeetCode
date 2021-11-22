class Solution {
    public int numDecodings(String s) {
        if (s.length() == 1) return calc(s, 0, 0);
        int[] arr = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            if (i == 0) {
                arr[i] = calc(s, i, i);
            } else if (i == 1) {
                arr[i] = arr[i-1] * calc(s, i, i) + (s.charAt(i-1) == '0' ? 0 : 1) * calc(s, i-1, i);
            } else {
                arr[i] = arr[i-1] * calc(s, i, i) + (s.charAt(i-1) == '0' ? 0 : arr[i-2]) * calc(s, i-1, i);
            }
        }
        return arr[s.length()-1];
    }

    private int calc(String s, int start, int end) {
        int temp = Integer.parseInt(s.substring(start, end+1));
        return (temp > 0 && temp <= 26) ? 1 : 0;
    }
}