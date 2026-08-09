import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for s, d, price in flights:
            adj[s].append((d, price))
        
        # Initialize a heap with (cost, current node, number of stops)
        stk = [(0, src, 0)]
        
        # Dictionary to store the cheapest price to reach each node with up to `k` stops
        cheapest = {}
        
        while stk:
            cost, s, stops = heapq.heappop(stk)
            
            # If the current node is the destination and within the allowed stops, return the cost
            if s == dst and stops <= k + 1:
                return cost
            
            # If we already have a cheaper way to get here with the same or fewer stops, skip
            if s in cheapest and cheapest[s] <= stops:
                continue
            
            # Update the cheapest stops for the current node
            cheapest[s] = stops
            
            # If we haven't exceeded the stop limit, explore neighbors
            if stops <= k:
                for d, price in adj[s]:
                    heapq.heappush(stk, (cost + price, d, stops + 1))
        
        # If no path was found within the allowed stops, return -1
        return -1