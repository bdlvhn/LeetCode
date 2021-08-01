class Solution:
    total: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode):
            if not node:
                return

            dfs(node.right)
            self.total += node.val
            node.val = self.total
            dfs(node.left)
        
        dfs(root)
        return root