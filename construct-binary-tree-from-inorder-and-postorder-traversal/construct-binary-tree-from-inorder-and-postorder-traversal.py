class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            index = inorder.index(postorder.pop())

            node = TreeNode(inorder[index])
            node.right = self.buildTree(inorder[index+1:], postorder)
            node.left = self.buildTree(inorder[:index], postorder)

            return node