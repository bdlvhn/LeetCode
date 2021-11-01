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
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        return MergeTree(root1, root2);
    }

    private TreeNode MergeTree(TreeNode root1, TreeNode root2) {
        if (root1 == null & root2 == null) return null;

        TreeNode root = new TreeNode();
        root.val = (root1 != null? root1.val : 0) + (root2 != null? root2.val : 0);
        root.left = MergeTree(root1 != null? root1.left : null, root2 != null? root2.left : null);
        root.right = MergeTree(root1 != null? root1.right : null, root2 != null? root2.right : null);

        return root;
    }
}