class Solution:
    total: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def findSumTree(node: TreeNode) -> TreeNode:
            if node is None:
                return None

            node.right = findSumTree(node.right)
            self.total += node.val
            node.val = self.total
            node.left = findSumTree(node.left)
            return node

        return findSumTree(root)