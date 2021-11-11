class Solution {
    public boolean backspaceCompare(String s, String t) {
        return makeString(s).equals(makeString(t));
    }

    private String makeString(String s) {
        Stack<Character> stack = new Stack<>();
        char[] chars = s.toCharArray();
        for (char c : chars) {
            if (c == '#') {
                if (!stack.isEmpty()) { stack.pop(); }
            } else {
                stack.add(c);
            }
        }
        return stack.toString();
    }
}