class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=defaultdict(list)
        for src,dst in tickets:
            adj[src].append(dst)
        
        for src in adj:
            adj[src].sort(reverse=True)
        
        route=[]
        def dfs(src):
            while (adj[src]):
                source=adj[src].pop()
                dfs(source)
            route.append(src)
        dfs("JFK")
        return route[::-1]