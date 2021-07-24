class Solution:
    isBalanced: bool = True
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode, height: int) -> int:
            if not node:
                return height
            height += 1
            left, right = dfs(node.left, height), dfs(node.right, height)
            if abs(left - right) > 1:
                self.isBalanced = False
            return max(left, right)

        dfs(root, 0)
        return self.isBalanced
