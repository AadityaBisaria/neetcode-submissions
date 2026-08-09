class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        heap=[(0,0)] #dst,difference
        visit=set()
        res=0
        while len(visit)<N:
            diff,src=heapq.heappop(heap)
            if src in visit:
                continue
            visit.add(src)
            res+=diff
            for cost,nei in adj[src]:
                if nei not in visit:
                    heapq.heappush(heap,(cost,nei))
        return res
