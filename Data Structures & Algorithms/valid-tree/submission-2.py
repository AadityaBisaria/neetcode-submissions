class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj={i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited=set()
        def dfs(src,prev):   
            if src  in visited:
                return False
            visited.add(src)
            for pos in adj[src]:
                if pos==prev:
                    continue
                if not dfs(pos,src):
                    return False
            return True        
        return dfs(0,-1) and n==len(visited)
