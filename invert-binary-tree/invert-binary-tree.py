class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode) -> TreeNode:
            if not node:
                return None

            node.left, node.right = node.right, node.left
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node

        return dfs(root)
