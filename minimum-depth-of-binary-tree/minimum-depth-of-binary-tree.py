class Solution:
    depth: int = int(1e5) + 1

    def minDepth(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, height: int):
            if not node:
                return
            
            if not node.left and not node.right:
                self.depth = min(self.depth, height)
            dfs(node.left, height + 1)
            dfs(node.right, height + 1)

        dfs(root, 1)
        return self.depth if root else 0