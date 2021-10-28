class Solution {
    public String reverseWords(String s) {
        String[] splits = s.split(" ");
        StringBuilder result = new StringBuilder();

        for (String split : splits) {
            result.append(new StringBuilder(split).reverse().toString() + " ");
        }
        return result.toString().trim();
    }
}