class Solution:
    depth: int = 0
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node: Node, height: int):
            if not node:
                return
            
            height += 1
            self.depth = max(self.depth, height)
            if node.children:
                for child in node.children:
                    dfs(child, height)
        
        dfs(root, 0)
        return self.depth