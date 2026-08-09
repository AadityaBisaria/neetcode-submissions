class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj={i:[] for i in range(n)}
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        cycle=set()
        def dfs(course,par):
            
            if course in cycle:
                return False
            cycle.add(course)
            for nei in adj[course]:
                if nei==par:
                    continue
                if not dfs(nei,course):
                    return False
            return True
        


        return dfs(0,-1) and len(cycle)==n
