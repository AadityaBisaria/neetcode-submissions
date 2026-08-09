class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res=max(piles)
        l,r=math.ceil(sum(piles)/h),max(piles)
        while l<=r:
            hour=0
            mid=(l+r)//2
            for banana in piles:
                hour+=math.ceil(float(banana)/mid)

            if hour<=h:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res