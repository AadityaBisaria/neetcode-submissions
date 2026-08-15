import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans=[]
        for i in range(len(nums)):
            ans.append(-nums[i])

        heapq.heapify(ans)
        answer=-1        
        while k!=0:
            answer= -heapq.heappop(ans)
            k-=1
        return answer