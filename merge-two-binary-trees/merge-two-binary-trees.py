class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        def merge(a: TreeNode, b: TreeNode) -> TreeNode:
            if a is None and b is None:
                return None
            
            if a and b:
                node = TreeNode(a.val + b.val)
                node.left = merge(a.left, b.left)
                node.right = merge(a.right, b.right)
            elif a and not b:
                node = TreeNode(a.val)
                node.left = merge(a.left, None)
                node.right = merge(a.right, None)
            elif not a and b:
                node = TreeNode(b.val)
                node.left = merge(None, b.left)
                node.right = merge(None, b.right)
            return node

        return merge(root1,root2)