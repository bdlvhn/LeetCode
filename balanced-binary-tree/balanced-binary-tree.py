class Solution:
    min_height: int = -1
    max_height: int = -1
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right) + 1
        
        return check(root) != -1