class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=defaultdict(list)
        for source,dest,cost in flights:
           adj[source].append((dest,cost))
        print(adj)
        aadi=[(0,src,0)]#cost,dst
        visited={}
        while aadi:
            cost,dest,stops=heapq.heappop(aadi)
            if dest==dst:
                return cost
            if stops>k:
                continue
            if dest in visited and visited[dest] <= stops:
                continue
            visited[dest] = stops

            
            for nei,neicost in adj[dest]:
                heapq.heappush(aadi,(neicost+cost,nei,stops+1))
        return -1






            