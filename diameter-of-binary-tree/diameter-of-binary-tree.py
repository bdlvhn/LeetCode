class Solution:
    diameter: int = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.diameter = max(self.diameter, left + right + 2)
            
            return max(left, right) + 1
        
        dfs(root)
        return self.diameter