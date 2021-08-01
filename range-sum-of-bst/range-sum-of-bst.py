class Solution:
    total: int = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return
            
            if low <= node.val <= high:
                self.total += node.val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.total