/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumNumbers(TreeNode root) {
        return doSumNumbers(root, new StringBuffer());
    }

    private int doSumNumbers(TreeNode root, StringBuffer numbers) {
        StringBuffer sb = new StringBuffer(numbers);
        sb.append(root.val);

        if (root.left == null && root.right == null) {
            return Integer.parseInt(sb.toString());
        }
        
        return (root.left != null ? doSumNumbers(root.left, sb) : 0) +
                (root.right != null ? doSumNumbers(root.right, sb) : 0);
        
    }
}