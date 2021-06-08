class Solution:
    total: int = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root:
            self.rangeSumBST(root.right,low,high)
            if root.val >= low and root.val <= high:
                self.total += root.val
            self.rangeSumBST(root.left,low,high)
        return self.total