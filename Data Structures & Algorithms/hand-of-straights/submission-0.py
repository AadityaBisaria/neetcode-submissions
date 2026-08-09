from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False

        cache=Counter(hand)
        minHeap=list(cache.keys())
        heapq.heapify(minHeap)
        while minHeap:
            x=minHeap[0]
            for i in range(x,x+groupSize):
                if i not in cache:
                    return False
                cache[i]-=1
                if cache[i]==0:
                    if i!=minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
