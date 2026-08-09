class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower,upper=1,sum(piles)
         
        rate=upper
        while lower<=upper:
            mid=(upper+lower)//2
            total=0
            for banana in piles:
                total+= math.ceil(float(banana)/mid) 
            if total>h:
                lower=mid+1
            elif h>=total:
                upper=mid-1
                rate=mid
        return rate