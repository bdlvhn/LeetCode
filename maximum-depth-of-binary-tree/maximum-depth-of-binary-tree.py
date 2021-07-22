class Solution:
    depth: int = 0
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, height: int):
            if node.left is None and node.right is None:
                self.depth = max(self.depth, height)
                return
            
            if node.left:
                dfs(node.left, height + 1)
            if node.right:
                dfs(node.right, height + 1)
        if root is None:
            return 0
        
        dfs(root, 1)
        return self.depth