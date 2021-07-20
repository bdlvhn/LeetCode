class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS + pruning
        graph = collections.defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        trace = set()
        visited = set()
        
        def dfs(x):
            if x in trace:
                return False
                
            if x in visited:
                return True
            
            trace.add(x)
            for y in graph[x]:
                if not dfs(y):
                    return False
            
            trace.remove(x)
            visited.add(x)
            return True
        
        for i in list(graph):
            if not dfs(i):
                return False
        
        return True