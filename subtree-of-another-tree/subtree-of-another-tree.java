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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode now = queue.poll();
            if (check(now, subRoot)) {
                return true;
            } else {
                if (now.left != null) queue.add(now.left);
                if (now.right != null) queue.add(now.right);
            }
        }
        return false;
    }

    private boolean check(TreeNode node1, TreeNode node2) {
        if (node1 == null ^ node2 == null) return false;
        if (node1 == null && node2 == null) return true;
        if (node1.val == node2.val && check(node1.left, node2.left) && check(node1.right, node2.right)) return true;
        return false;
    }
}