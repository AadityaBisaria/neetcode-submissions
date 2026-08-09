import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={i :[] for i in range(1,n+1)}
        for src,dst,wt in times:
            adj[src].append((dst,wt))
        
        fastest={}
        minheap=[(0,k)]
        while minheap:
            time1, src=heapq.heappop(minheap)
            if src  in fastest:
                continue
            fastest[src]=time1
            
            for n1,time2 in adj[src]:
                if n1 not in fastest:
                    heapq.heappush(minheap,(time2+time1,n1))
            
        for i in range(1,n+1):
            if i not in fastest:
                return -1
        return max(fastest.values())
            