class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minheap=[]
        res=[]
        for left,right in intervals:
            heapq.heappush(minheap,(right-left+1,[left,right]))

        for q in queries:
            otherheap=[]
            while minheap:
                length,rangee=minheap[0]
                left,right=rangee
                
                if q>=left and q<=right:
                    res.append(length)
                    break
                else:
                    otherheap.append(heapq.heappop(minheap))
            if not minheap:
                res.append(-1)
            for value in otherheap:
                heapq.heappush(minheap,value)
            
        return res